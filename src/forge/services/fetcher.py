import shutil
import zipfile
import tempfile
import httpx
import typer
import sys
from pathlib import Path
from typing import Tuple

from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

from forge.utils import console, StepTracker, handle_vscode_settings, _github_auth_headers

def copy_local_template(
    project_path: Path,
    ai_assistant: str,
    script_type: str,
    is_current_dir: bool = False,
    *,
    tracker: StepTracker | None = None,
    debug: bool = False,
) -> Path:
    """Copy templates from local source instead of downloading."""

    # Improved path resolution
    potential_roots = [
        Path.cwd(),
        Path(__file__).parent.parent.parent.parent, # src/forge/services/fetcher.py -> root
    ]

    # Attempt to find installed location if not found in dev paths
    if hasattr(sys, 'prefix'):
        potential_roots.append(Path(sys.prefix) / "share" / "forge")

    templates_root = None
    for root in potential_roots:
        if (root / "templates").is_dir():
            templates_root = root / "templates"
            break

    if not templates_root:
        msg = f"Could not find 'templates' directory. Checked: {potential_roots}"
        if tracker:
            tracker.error("copy-local", msg)
        raise RuntimeError(msg)

    if tracker:
        tracker.start("copy-local", f"from {templates_root}")
    else:
        console.print(f"[cyan]Copying local templates from:[/cyan] {templates_root}")

    try:
        # Create destination directory
        if not is_current_dir:
            project_path.mkdir(parents=True, exist_ok=True)

        # 1. Copy common structure
        structure_dir = templates_root / "structure"
        if structure_dir.exists():
            _merge_directory(structure_dir, project_path, verbose=False, tracker=tracker)

        # 2. Copy agent specific config
        from forge.config import AGENT_CONFIG
        agent_config = AGENT_CONFIG.get(ai_assistant)
        if not agent_config:
             raise ValueError(f"Unknown agent: {ai_assistant}")

        agent_folder_name = agent_config["folder"].strip("/")

        agent_source = templates_root / agent_folder_name
        if not agent_source.exists():
            agent_source = templates_root / agent_folder_name.lstrip(".")

        if agent_source.exists():
             target_agent_dir = project_path / agent_folder_name
             if not target_agent_dir.exists():
                 target_agent_dir.mkdir(parents=True, exist_ok=True)
             _merge_directory(agent_source, target_agent_dir, verbose=False, tracker=tracker)

        if tracker:
            tracker.complete("copy-local", "done")

    except Exception as e:
        if tracker:
            tracker.error("copy-local", str(e))
        raise

    return project_path


def _merge_directory(src: Path, dst: Path, verbose: bool = False, tracker: StepTracker = None):
    """Recursively merge src directory into dst directory."""
    for item in src.iterdir():
        dest_path = dst / item.name
        if item.is_dir():
            if not dest_path.exists():
                dest_path.mkdir(parents=True, exist_ok=True)
            _merge_directory(item, dest_path, verbose, tracker)
        else:
            if dest_path.exists():
                 if dest_path.name == "settings.json" and dest_path.parent.name == ".vscode":
                     handle_vscode_settings(item, dest_path, dest_path.relative_to(dst), verbose, tracker)
                 else:
                     shutil.copy2(item, dest_path)
            else:
                 shutil.copy2(item, dest_path)


def download_template_from_github(
    ai_assistant: str,
    download_dir: Path,
    *,
    script_type: str = "sh",
    verbose: bool = True,
    show_progress: bool = True,
    client: httpx.Client = None,
    debug: bool = False,
    github_token: str = None,
) -> Tuple[Path, dict]:
    repo_owner = "suportesaude"
    repo_name = "forge"

    if client is None:
        import ssl
        import truststore
        ssl_context = truststore.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        client = httpx.Client(verify=ssl_context)

    if verbose:
        console.print("[cyan]Fetching latest release information...[/cyan]")
    api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"

    try:
        response = client.get(
            api_url,
            timeout=30,
            follow_redirects=True,
            headers=_github_auth_headers(github_token),
        )
        status = response.status_code
        if status != 200:
            msg = f"GitHub API returned {status} for {api_url}"
            if debug:
                msg += f"\nResponse headers: {response.headers}\nBody (truncated 500): {response.text[:500]}"
            raise RuntimeError(msg)
        try:
            release_data = response.json()
        except ValueError as je:
            raise RuntimeError(
                f"Failed to parse release JSON: {je}\nRaw (truncated 400): {response.text[:400]}"
            )
    except Exception as e:
        console.print(f"[red]Error fetching release information[/red]")
        console.print(Panel(str(e), title="Fetch Error", border_style="red"))
        raise typer.Exit(1)

    assets = release_data.get("assets", [])
    pattern = f"forge-kit-template-{ai_assistant}-{script_type}"
    matching_assets = [
        asset
        for asset in assets
        if pattern in asset["name"] and asset["name"].endswith(".zip")
    ]

    asset = matching_assets[0] if matching_assets else None

    if asset is None:
        console.print(
            f"[red]No matching release asset found[/red] for [bold]{ai_assistant}[/bold] (expected pattern: [bold]{pattern}[/bold])"
        )
        asset_names = [a.get("name", "?") for a in assets]
        console.print(
            Panel(
                "\n".join(asset_names) or "(no assets)",
                title="Available Assets",
                border_style="yellow",
            )
        )
        raise typer.Exit(1)

    download_url = asset["browser_download_url"]
    filename = asset["name"]
    file_size = asset["size"]

    if verbose:
        console.print(f"[cyan]Found template:[/cyan] {filename}")
        console.print(f"[cyan]Size:[/cyan] {file_size:,} bytes")
        console.print(f"[cyan]Release:[/cyan] {release_data['tag_name']}")

    zip_path = download_dir / filename
    if verbose:
        console.print(f"[cyan]Downloading template...[/cyan]")

    try:
        with client.stream(
            "GET",
            download_url,
            timeout=60,
            follow_redirects=True,
            headers=_github_auth_headers(github_token),
        ) as response:
            if response.status_code != 200:
                body_sample = response.text[:400]
                raise RuntimeError(
                    f"Download failed with {response.status_code}\nHeaders: {response.headers}\nBody (truncated): {body_sample}"
                )
            total_size = int(response.headers.get("content-length", 0))
            with open(zip_path, "wb") as f:
                if total_size == 0:
                    for chunk in response.iter_bytes(chunk_size=8192):
                        f.write(chunk)
                else:
                    if show_progress:
                        with Progress(
                            SpinnerColumn(),
                            TextColumn("[progress.description]{task.description}"),
                            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
                            console=console,
                        ) as progress:
                            task = progress.add_task("Downloading...", total=total_size)
                            downloaded = 0
                            for chunk in response.iter_bytes(chunk_size=8192):
                                f.write(chunk)
                                downloaded += len(chunk)
                                progress.update(task, completed=downloaded)
                    else:
                        for chunk in response.iter_bytes(chunk_size=8192):
                            f.write(chunk)
    except Exception as e:
        console.print(f"[red]Error downloading template[/red]")
        detail = str(e)
        if zip_path.exists():
            zip_path.unlink()
        console.print(Panel(detail, title="Download Error", border_style="red"))
        raise typer.Exit(1)
    if verbose:
        console.print(f"Downloaded: {filename}")
    metadata = {
        "filename": filename,
        "size": file_size,
        "release": release_data["tag_name"],
        "asset_url": download_url,
    }
    return zip_path, metadata


def download_and_extract_template(
    project_path: Path,
    ai_assistant: str,
    script_type: str,
    is_current_dir: bool = False,
    *,
    verbose: bool = True,
    tracker: StepTracker | None = None,
    client: httpx.Client = None,
    debug: bool = False,
    github_token: str = None,
) -> Path:
    """Download the latest release and extract it to create a new project."""
    current_dir = Path.cwd()

    if tracker:
        tracker.start("fetch", "contacting GitHub API")
    try:
        zip_path, meta = download_template_from_github(
            ai_assistant,
            current_dir,
            script_type=script_type,
            verbose=verbose and tracker is None,
            show_progress=(tracker is None),
            client=client,
            debug=debug,
            github_token=github_token,
        )
        if tracker:
            tracker.complete(
                "fetch", f"release {meta['release']} ({meta['size']:,} bytes)"
            )
            tracker.add("download", "Download template")
            tracker.complete("download", meta["filename"])
    except Exception as e:
        if tracker:
            tracker.error("fetch", str(e))
        else:
            if verbose:
                console.print(f"[red]Error downloading template:[/red] {e}")
        raise

    if tracker:
        tracker.add("extract", "Extract template")
        tracker.start("extract")
    elif verbose:
        console.print("Extracting template...")

    try:
        if not is_current_dir:
            project_path.mkdir(parents=True)

        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_contents = zip_ref.namelist()
            if tracker:
                tracker.start("zip-list")
                tracker.complete("zip-list", f"{len(zip_contents)} entries")
            elif verbose:
                console.print(f"[cyan]ZIP contains {len(zip_contents)} items[/cyan]")

            if is_current_dir:
                with tempfile.TemporaryDirectory() as temp_dir:
                    temp_path = Path(temp_dir)
                    zip_ref.extractall(temp_path)

                    extracted_items = list(temp_path.iterdir())
                    if tracker:
                        tracker.start("extracted-summary")
                        tracker.complete(
                            "extracted-summary", f"temp {len(extracted_items)} items"
                        )
                    elif verbose:
                        console.print(
                            f"[cyan]Extracted {len(extracted_items)} items to temp location[/cyan]"
                        )

                    source_dir = temp_path
                    if len(extracted_items) == 1 and extracted_items[0].is_dir():
                        source_dir = extracted_items[0]
                        if tracker:
                            tracker.add("flatten", "Flatten nested directory")
                            tracker.complete("flatten")
                        elif verbose:
                            console.print(
                                f"[cyan]Found nested directory structure[/cyan]"
                            )

                    for item in source_dir.iterdir():
                        dest_path = project_path / item.name
                        if item.is_dir():
                            if dest_path.exists():
                                if verbose and not tracker:
                                    console.print(
                                        f"[yellow]Merging directory:[/yellow] {item.name}"
                                    )
                                for sub_item in item.rglob("*"):
                                    if sub_item.is_file():
                                        rel_path = sub_item.relative_to(item)
                                        dest_file = dest_path / rel_path
                                        dest_file.parent.mkdir(
                                            parents=True, exist_ok=True
                                        )
                                        if (
                                            dest_file.name == "settings.json"
                                            and dest_file.parent.name == ".vscode"
                                        ):
                                            handle_vscode_settings(
                                                sub_item,
                                                dest_file,
                                                rel_path,
                                                verbose,
                                                tracker,
                                            )
                                        else:
                                            shutil.copy2(sub_item, dest_file)
                            else:
                                shutil.copytree(item, dest_path)
                        else:
                            if dest_path.exists() and verbose and not tracker:
                                console.print(
                                    f"[yellow]Overwriting file:[/yellow] {item.name}"
                                )
                            shutil.copy2(item, dest_path)
                    if verbose and not tracker:
                        console.print(
                            f"[cyan]Template files merged into current directory[/cyan]"
                        )
            else:
                zip_ref.extractall(project_path)

                extracted_items = list(project_path.iterdir())
                if tracker:
                    tracker.start("extracted-summary")
                    tracker.complete(
                        "extracted-summary", f"{len(extracted_items)} top-level items"
                    )
                elif verbose:
                    console.print(
                        f"[cyan]Extracted {len(extracted_items)} items to {project_path}:[/cyan]"
                    )
                    for item in extracted_items:
                        console.print(
                            f"  - {item.name} ({'dir' if item.is_dir() else 'file'})"
                        )

                if len(extracted_items) == 1 and extracted_items[0].is_dir():
                    nested_dir = extracted_items[0]
                    temp_move_dir = project_path.parent / f"{project_path.name}_temp"

                    shutil.move(str(nested_dir), str(temp_move_dir))

                    project_path.rmdir()

                    shutil.move(str(temp_move_dir), str(project_path))
                    if tracker:
                        tracker.add("flatten", "Flatten nested directory")
                        tracker.complete("flatten")
                    elif verbose:
                        console.print(
                            f"[cyan]Flattened nested directory structure[/cyan]"
                        )

    except Exception as e:
        if tracker:
            tracker.error("extract", str(e))
        else:
            if verbose:
                console.print(f"[red]Error extracting template:[/red] {e}")
                if debug:
                    console.print(
                        Panel(str(e), title="Extraction Error", border_style="red")
                    )

        if not is_current_dir and project_path.exists():
            shutil.rmtree(project_path)
        raise typer.Exit(1)
    else:
        if tracker:
            tracker.complete("extract")
    finally:
        if tracker:
            tracker.add("cleanup", "Remove temporary archive")

        if zip_path.exists():
            zip_path.unlink()
            if tracker:
                tracker.complete("cleanup")
            elif verbose:
                console.print(f"Cleaned up: {zip_path.name}")

    return project_path
