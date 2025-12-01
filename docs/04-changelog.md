# 04 Changelog: Institutional Memory

**Status**: Append-Only
**Purpose**: Record what changed, WHY, and what we learned.

## Template
```markdown
### [YYYY-MM-DD] Title of Change
- **What**: Brief description of code changes.
- **Why**: The business or technical reason.
- **Mistake/Learning**: (Optional) What went wrong that we should avoid next time?
```

## Log

### 2024-05-22 Documentation Refactor
- **What**: Migrated documentation to FORGE v2 structure (`00-07` files). Created `AGENTS.md`.
- **Why**: To align the project with the new methodology and ensure AI Agents have precise context.
- **Learning**: The previous docs were fragmented; strict ordering helps agents ingest context sequentially.
