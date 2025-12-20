# Screen: [Screen Name]

**ID**: `SCR-[00X]`
**Route**: `/path/to/screen`
**Status**: Draft / Planned / Implemented

## 1. Purpose
*Describe the primary goal of this screen. What does the user achieve here?*

## 2. Look and Feel
*Describe the visual style, layout, and mood. Reference the Design System.*
- **Layout**: [e.g., Dashboard Layout, Two-Column]
- **Theme**: [e.g., Light/Dark, specific color scheme]

## 3. Component Tree (Atomic Breakdown)

### Organisms (Sections)
*List the major sections of the page.*
- **[Org-1] Header**: Standard app header.
- **[Org-2] UserStats**: Displays charts and metrics.
  - **Molecules**: `StatCard`, `DateRangePicker`
    - **Atoms**: `Icon`, `Text`, `Button`
- **[Org-3] ActionPanel**: Form for user actions.

### Molecules (New/Specific)
*List any new molecules required specifically for this screen.*

### Atoms (New/Specific)
*List any new atoms required.*

## 4. Interactions
*Describe user interactions.*
- **[Action 1]**: When user clicks X, Y happens.
- **[Action 2]**: Validation rules for form Z.

## 5. Data Requirements
*What data is needed?*
- **Queries**: `getUserProfile`, `getStats`
- **Mutations**: `updateSettings`

## 6. Implementation Plan
1. [ ] Create Atoms: ...
2. [ ] Create Molecules: ...
3. [ ] Assemble Organisms: ...
4. [ ] Construct Page: ...
