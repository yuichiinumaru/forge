# Atomic Design & Parallelism

## Hierarchy

1.  **Atoms** (No logic, purely visual)
    -   Examples: Buttons, Inputs, Labels, Icons.
    -   Properties: Highly reusable, no business logic, stateless (mostly).
2.  **Molecules** (Composites, dumb)
    -   Examples: SearchBar (Input + Button), FormField (Label + Input + Error).
    -   Properties: Composed of atoms, no business logic, driven by props.
3.  **Organisms** (Business logic/State)
    -   Examples: UserList, Header, Footer, LoginForm.
    -   Properties: Connected to state/store, contains business logic, composes molecules and atoms.
4.  **Templates/Pages**
    -   Examples: DashboardLayout, UserProfilePage.
    -   Properties: Layouts, routing targets.

## Rule of Gold

**Explicit Interfaces**: Atoms and Molecules **MUST** define their Interface (Props) *before* implementation to allow parallel work.
-   This contract allows the implementation of the component to proceed in parallel with its consumption.
-   Props must be strictly typed (TypeScript interfaces, Swift protocols, PropTypes, etc.).

## Parallelism Score

-   **Atoms**: **High**. Can be implemented by any agent immediately. No dependencies.
-   **Molecules**: **Medium**. Depends on Atoms. Interfaces allow parallel work.
-   **Organisms**: **Low**. Depends on Molecules and Business Logic. High complexity.

To maximize parallelism, tasks should be broken down such that Atoms are cleared first, unlocking Molecules, which unlock Organisms.
