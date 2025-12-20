# Atomic Design System Rules

## Core Philosophy
We strictly follow **Atomic Design** to decompose UIs into five hierarchical levels. This maximizes parallel development and reusability.

## The Hierarchy

1.  **Atoms** 🧪 (Indivisible)
    -   *Definition*: Smallest building blocks. No business logic. Purely visual.
    -   *Examples*: Button, Input, Label, Icon, Typography.
    -   *Rule*: Must have strict Prop Interfaces. Must be reusable in 3+ places.

2.  **Molecules** 🔗 (Simple Groups)
    -   *Definition*: Groups of atoms functioning together. No complex business logic.
    -   *Examples*: SearchBar (Input + Button), FormField (Label + Input + Error).
    -   *Rule*: Combine related atoms. Single responsibility.

3.  **Organisms** 🧬 (Complex Sections)
    -   *Definition*: Groups of molecules/atoms forming distinct UI sections. Can have state/business logic.
    -   *Examples*: Header, ProductList, LoginForm, Sidebar.
    -   *Rule*: Orchestrate molecules. Handle state. Dependency Injection for data.

4.  **Templates** 📐 (Layouts)
    -   *Definition*: Page structures without real content.
    -   *Examples*: DashboardLayout, AuthLayout.
    -   *Rule*: Define grid/flex structures. No hardcoded content.

5.  **Pages** 🖼️ (Instances)
    -   *Definition*: Templates populated with real content.
    -   *Examples*: HomePage, UserProfile.
    -   *Rule*: Realistic data. Integration testing.

## Golden Rules for Agents

1.  **Composition over Configuration**: Build complex components from simpler ones, not via 100 props.
2.  **Single Responsibility**: One component, one job.
3.  **Props Contracts**: Define interfaces (TypeScript/PropTypes) *before* implementation.
4.  **Accessibility (a11y)**: Mandatory WCAG 2.1 AA compliance (ARIA, keyboard nav).
5.  **No Logic in Atoms**: Atoms are dumb. Logic belongs in Organisms/Hooks.
6.  **Parallelism**: Implement Atoms first, then Molecules, then Organisms.

## File Structure
```
src/components/
  atoms/       # Button/Button.tsx
  molecules/   # SearchBar/SearchBar.tsx
  organisms/   # Header/Header.tsx
  templates/   # DashboardLayout/DashboardLayout.tsx
  pages/       # HomePage/HomePage.tsx
```
