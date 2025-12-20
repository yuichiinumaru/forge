# Forge CLI Design System

## 1. Introduction
Forge uses a **Text User Interface (TUI)** Design System powered by `rich` and `typer`. This system ensures consistency across all CLI commands.

## 2. Design Tokens (Atoms)

### Colors
- **Primary Action**: `cyan` (Prompts, Highlights)
- **Success**: `green` (Completed steps, Success messages)
- **Error**: `red` (Failures, Exceptions)
- **Warning**: `yellow` (Skips, Alerts)
- **Text**: `white` (Primary text)
- **Dim**: `bright_black` (Details, Logs)

### Symbols
- **Success**: `●` (Green) or `✓`
- **Pending**: `○` (Dim Green)
- **Error**: `●` (Red) or `✗`

### Typography
- **Headings**: Bold, Underlined (rarely used in CLI, mostly for Banners)
- **Banner**: ASCII Art + Tagline

## 3. Components (Molecules)

### StepTracker (`utils.StepTracker`)
- **Purpose**: Displays progress of long-running operations.
- **Composition**: Tree structure + Symbols + Labels + Details.
- **States**: Pending, Running, Done, Error, Skipped.

### Selection Panel (`utils.select_with_arrows`)
- **Purpose**: Interactive choice selection.
- **Composition**: `Panel` + `Table` (Grid) + Cursor (`▶`).
- **Interaction**: Arrow keys + Enter.

### Banner (`utils.show_banner`)
- **Purpose**: Brand identity on startup.
- **Composition**: ASCII Art + Tagline (Italic Yellow).

## 4. Layouts (Organisms)

### Command Flow
1. **Banner**: Always shown at start (optional).
2. **Input Phase**: User prompts (Selection Panel).
3. **Execution Phase**: StepTracker showing progress.
4. **Result Phase**: Final success/error message.

## 5. Usage Rules
- Always use `StepTracker` for multi-step operations.
- Use `select_with_arrows` for any choice > 2 options.
- Maintain color semantics (Red = Error).
