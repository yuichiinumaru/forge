# Rust Development Rules

## Cargo
- Use `Cargo.toml` for dependencies.
- Run `cargo fmt` and `cargo clippy` before committing.

## Safety
- Minimize usage of `unsafe`.
- Handle all `Result` and `Option` types (no `.unwrap()` in production code).

## Testing
- Unit tests in the same file (module `tests`).
- Integration tests in `tests/` directory.
- Run tests: `cargo test`.

## Style
- Types: `PascalCase`.
- Functions/Variables: `snake_case`.
