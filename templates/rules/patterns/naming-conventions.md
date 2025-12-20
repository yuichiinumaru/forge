# Hierarchical Naming Conventions

## Principle
We enforce a strict, hierarchical naming convention to ensure consistency and coherence across the codebase. Names should read like a path or a sentence that describes the entity's place in the system.

## Pattern
`Domain.Entity.State` or `Domain.Component.SubComponent`

## Examples
- **State Machines**: `ChessServer.Game.Started`, `OrderSystem.Payment.Pending`
- **Classes/Modules**: `Forge.CLI.Workflow`, `Forge.Compiler.Markdown`
- **UI Components**: `DesignSystem.Atoms.Button`, `Dashboard.Header.UserProfile`

## Rules
1.  **Dot Notation** (Conceptual): Even if the language uses other separators (like `/` for folders or `_` for files), conceptualize the name as a hierarchy.
2.  **Context First**: Always prefix with the broader context. `Game.Started` is better than `StartedGame`.
3.  **Consistency**: Use the same hierarchy across filenames, class names, and variable names where possible.
    -   File: `chess_server/game/started.py`
    -   Class: `ChessServerGameStarted` (or `Started` inside `Game` namespace)
4.  **No Ambiguity**: Avoid generic names like `Manager`, `Handler` unless scoped (e.g., `Session.Manager` is okay, `Manager` is not).
