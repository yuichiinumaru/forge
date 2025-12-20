# **Atomic Design System Fundamentals for AI Coding Agents**

### **PART 1: THE FIVE HIERARCHICAL STAGES**

#### **1. ATOMS** 🧪

**Definition:** The smallest, indivisible UI building blocks that cannot be broken down further.

**Examples:**

- Buttons
- Form inputs (text fields, checkboxes, radio buttons)
- Icons
- Typography (headings, paragraphs)
- Color palettes
- Spacing tokens
- Borders and shadows
- Labels
- Links

**Rules for AI Agents:**

- ✅ **NEVER mix concerns** - One atom = one single responsibility
- ✅ **ALWAYS make them reusable** - If you can't use it in 3+ places, consider if it's truly atomic
- ✅ **Document default states** - normal, hover, focus, disabled, loading, error
- ✅ **Create strict prop interfaces** - Every atom must have a clear, limited API
- ✅ **Include accessibility attributes** - `aria-label`, `aria-describedby`, roles
- ❌ **NEVER embed atoms with business logic** - Keep them purely presentational
- ❌ **NEVER create "god atoms"** - If complexity grows, it's become a molecule
- ❌ **NEVER skip prop validation** - Type-check everything (TypeScript required)

***

#### **2. MOLECULES** 🔗

**Definition:** Simple components formed by combining 2-3 atoms serving a specific function.

**Examples:**

- Search bar (input + icon + button)
- Form field (label + input + helper text)
- Navigation item (icon + text + link)
- Card header (title + close button)
- Tag (icon + text + delete button)

**Rules for AI Agents:**

- ✅ **Combine related atoms only** - Atoms that work together logically
- ✅ **Maintain single responsibility** - One primary function per molecule
- ✅ **Accept atoms as props, not primitives** - Enforce composition
- ✅ **Document composition patterns** - Show which atoms combine and why
- ✅ **Test all atom combinations** - Verify edge cases
- ✅ **Keep prop interfaces simple** - Max 5-7 props per molecule
- ❌ **NEVER include conditional logic for business rules** - That belongs in organisms
- ❌ **NEVER hardcode styles** - Always accept theme/styling props
- ❌ **NEVER skip documentation of props** - Every prop needs a comment
- ❌ **NEVER create "helper molecules"** - If it doesn't appear in UI, it's not a molecule

***

#### **3. ORGANISMS** 🧬

**Definition:** Relatively complex components combining molecules and atoms to form distinct sections.

**Examples:**

- Header (logo + nav menu + user profile)
- Search results list (search molecule + result cards + pagination)
- Form (multiple form field molecules + submit button)
- Data table (headers + rows + sorting controls)
- Modal dialog (title + content area + footer buttons)
- Sidebar navigation (navigation items + user info)

**Rules for AI Agents:**

- ✅ **Orchestrate molecules** - Primary job is coordinating smaller pieces
- ✅ **Handle state management** - Organisms can have local state
- ✅ **Accept business logic props** - Event handlers, callbacks, data formatters
- ✅ **Implement proper error boundaries** - Handle edge cases gracefully
- ✅ **Document state management** - Show how state flows through children
- ✅ **Include comprehensive examples** - Show typical use cases
- ✅ **Write integration tests** - Test molecules together
- ❌ **NEVER fetch data directly** - Data should come via props (dependency injection)
- ❌ **NEVER hardcode values** - All data should be configurable
- ❌ **NEVER skip accessibility testing** - Complex interactions need WCAG compliance
- ❌ **NEVER create organisms with 10+ molecules** - Split into multiple components

***

#### **4. TEMPLATES** 📐

**Definition:** Layout skeletons showing how organisms and molecules combine to form page structure.

**Examples:**

- Dashboard layout (sidebar + header + main content area)
- Blog post layout (header + article section + sidebar)
- E-commerce product page (header + product images + details + reviews)
- Admin panel layout (navigation + breadcrumbs + content + footer)
- Authentication flow (centered form container)

**Rules for AI Agents:**

- ✅ **Define content structure, not actual content** - Use placeholders/slots
- ✅ **Show layout without real data** - Demonstrate structure only
- ✅ **Document layout variations** - Different screen sizes, content types
- ✅ **Use CSS Grid/Flexbox patterns** - Reusable layout logic
- ✅ **Include responsive breakpoints** - Mobile, tablet, desktop variations
- ✅ **Show slot/children acceptance** - Clear where content goes
- ❌ **NEVER include hard-coded content** - Keep templates empty shells
- ❌ **NEVER mix layout with styling** - Separate structure from appearance
- ❌ **NEVER skip responsive design** - All templates must adapt to screen sizes
- ❌ **NEVER create overly specific templates** - Keep reusable across different pages

***

#### **5. PAGES** 🖼️

**Definition:** Specific instances of templates with real content, demonstrating final UI and variations.

**Examples:**

- Homepage with actual marketing copy
- User profile page with real user data
- Product listing with actual products
- Blog post with published article content
- Dashboard with live metrics

**Rules for AI Agents:**

- ✅ **Use real data or realistic mocks** - Test with production-like scenarios
- ✅ **Document variations** - Empty states, loading states, error states, success states
- ✅ **Show edge cases** - Long text, missing data, truncation scenarios
- ✅ **Test with actual content** - Ensure design survives real usage
- ✅ **Verify all interactions work** - End-to-end functionality testing
- ✅ **Include accessibility testing results** - WCAG compliance proof
- ❌ **NEVER use placeholder content in production** - Always real or realistic
- ❌ **NEVER skip error states** - Show broken links, failed loads, missing data
- ❌ **NEVER skip loading states** - Show skeletal loading, spinners, placeholders
- ❌ **NEVER skip responsive testing** - Test all breakpoints with real content

***

### **PART 2: CRITICAL RULES FOR AI CODING AGENTS (NEVER FORGET)**

#### **A. COMPOSITION OVER CONFIGURATION** 🎯

**Rule:** Always prefer building complex components from simpler ones rather than creating single components with many configuration options.

```javascript
// ❌ BAD: Configuration hell
<Card
  hasImage={true}
  hasTitle={true}
  hasDescription={true}
  hasButton={true}
  buttonText="Click"
  imagePosition="top"
  layout="vertical"
/>

// ✅ GOOD: Composition
<Card>
  <CardImage src="..." />
  <CardTitle>Title</CardTitle>
  <CardDescription>Description</CardDescription>
  <CardButton>Click</CardButton>
</Card>
```

**Why:** Configuration grows exponentially complex. Composition stays predictable. "God components" are maintenance nightmares.

***

#### **B. SINGLE RESPONSIBILITY PRINCIPLE (SRP)** 🎪

**Rule:** Each component must have ONE reason to change.

```javascript
// ❌ BAD: Multiple responsibilities
function UserProfile({ userId, theme, layout, onUpdate, onDelete, permissions }) {
  // Fetches data, handles auth, manages UI state, enforces permissions...
}

// ✅ GOOD: Single responsibility
function UserProfileView({ user, onUpdate, onDelete }) {
  // Only displays user info
}
// Usage:
<UserProfileContainer userId={id}>
  <UserProfileView {...props} />
</UserProfileContainer>
```

**Why:** Easy to test, understand, modify. Low cognitive load. Reusable in different contexts.

***

#### **C. PROP INTERFACE CONTRACTS** 📋

**Rule:** Every component must explicitly document and type its props. No exceptions.

```typescript
// ✅ GOOD: Clear contract
interface ButtonProps {
  /** The button text or icon */
  children: React.ReactNode;

  /** Button style variant */
  variant?: 'primary' | 'secondary' | 'danger';

  /** Button size */
  size?: 'sm' | 'md' | 'lg';

  /** Click handler */
  onClick?: (e: React.MouseEvent) => void;

  /** Disabled state */
  disabled?: boolean;

  /** Loading state */
  isLoading?: boolean;
}

export const Button: React.FC<ButtonProps> = ({
  children,
  variant = 'primary',
  size = 'md',
  onClick,
  disabled = false,
  isLoading = false,
}) => { ... }
```

**Why:** Prevents misuse. Self-documents. Enables type checking. IDE auto-completion. Future maintainers know exactly what props to pass.

***

#### **D. DEPENDENCY INJECTION (NOT DATA FETCHING)** 💉

**Rule:** Components receive data via props, never fetch it themselves.

```javascript
// ❌ BAD: Component is tightly coupled to data source
function UserList() {
  const [users, setUsers] = useState([]);
  useEffect(() => {
    fetchUsers().then(setUsers); // Tightly coupled!
  }, []);
  return users.map(user => <UserItem {...user} />);
}

// ✅ GOOD: Data passed in, component doesn't care about source
function UserList({ users }) {
  return users.map(user => <UserItem {...user} />);
}

// ✅ Usage:
function UserListContainer() {
  const [users, setUsers] = useState([]);
  useEffect(() => {
    fetchUsers().then(setUsers); // Fetch here
  }, []);
  return <UserList users={users} />;
}
```

**Why:** Testable without mocking APIs. Reusable in different contexts. Clear data flow. Easy to maintain.

***

#### **E. ACCESSIBILITY IS MANDATORY** ♿

**Rule:** Every component must be WCAG 2.1 Level AA compliant. Not optional.

```javascript
// ❌ BAD: Not accessible
<div onClick={handleClick}>Delete</div>

// ✅ GOOD: Accessible
<button
  onClick={handleClick}
  aria-label="Delete this item"
>
  Delete
</button>

// ✅ For complex components:
<div role="region" aria-label="Search results">
  <h2 id="results-heading">Search Results</h2>
  <div aria-labelledby="results-heading">
    {results.map(result => (
      <article key={result.id} {...accessibilityProps}>
        {result.title}
      </article>
    ))}
  </div>
</div>
```

**Requirements:**

- Keyboard navigation (Tab, Enter, Arrow keys work)
- Screen reader support (proper ARIA labels and roles)
- Color contrast (4.5:1 for normal text, 3:1 for large)
- Focus visible (never remove focus outline)
- Semantic HTML (button, link, form elements are actual elements)

***

#### **F. IMMUTABILITY \& STATE MANAGEMENT** 🔒

**Rule:** Never mutate state directly. Always create new objects/arrays.

```javascript
// ❌ BAD: Mutating state
const user = state.user;
user.name = "New Name";
setState(state); // Won't trigger re-render

// ✅ GOOD: Immutable updates
setState({
  ...state,
  user: {
    ...state.user,
    name: "New Name"
  }
});

// ✅ EVEN BETTER: Use update patterns
setState(produce(state, draft => {
  draft.user.name = "New Name";
}));
```

**Why:** Predictable re-renders. Enables time-travel debugging. Prevents hard-to-find bugs. Essential for React/Vue/etc.

***

#### **G. DOCUMENTATION IS CODE** 📚

**Rule:** Every component needs:

1. **Purpose statement** - What does it do?
2. **Usage example** - How do you use it?
3. **Props documentation** - What props exist?
4. **Variants documentation** - What states exist?
5. **Accessibility notes** - Any special considerations?
```typescript
/**
 * Button Component
 *
 * Primary interactive element for user actions. Supports multiple variants,
 * sizes, and loading states.
 *
 * @example
 * // Basic usage
 * <Button onClick={handleClick}>Click Me</Button>
 *
 * @example
 * // With variants
 * <Button variant="primary">Primary</Button>
 * <Button variant="danger">Delete</Button>
 *
 * @example
 * // Loading state
 * <Button isLoading>Processing...</Button>
 *
 * Accessibility:
 * - Always include aria-label for icon-only buttons
 * - Focus outline is always visible
 * - Keyboard navigable (Space/Enter to activate)
 */
export const Button: React.FC<ButtonProps> = (props) => { ... }
```

**Why:** Future you won't remember. Team members won't guess. New maintainers can onboard. Living documentation.

***

#### **H. CONSISTENT NAMING CONVENTIONS** 📛

**Rule:** Follow strict naming patterns everywhere.

```javascript
// ✅ GOOD: Consistent, predictable naming

// Components: PascalCase
- Button
- UserCard
- SearchInput
- ModalDialog

// Props: camelCase
- onClick
- isLoading
- onSubmit
- isDarkMode

// State: camelCase, clear prefixes
- isOpen (boolean)
- hasError (boolean)
- isFetching (boolean)
- selectedUser (object/entity)
- userList (array)
- errorMessage (string)

// Folders: kebab-case
- /components/button
- /components/user-card
- /components/search-input

// Files: Follow folder structure
- /button/Button.tsx
- /button/button.styles.ts
- /button/Button.test.tsx
- /button/Button.stories.tsx
```

**Why:** Predictable. Easy to search and navigate. Clear intent. Reduces cognitive load.

***

#### **I. TESTING IS NOT OPTIONAL** 🧪

**Rule:** Every component must have tests for:

1. **Rendering** - Does it appear?
2. **Props** - Do props work correctly?
3. **User interactions** - Do clicks/inputs work?
4. **Accessibility** - Is it accessible?
5. **Edge cases** - What if data is missing/empty/invalid?
```typescript
describe('Button', () => {
  it('renders button with text', () => {
    render(<Button>Click Me</Button>);
    expect(screen.getByRole('button', { name: /click me/i })).toBeInTheDocument();
  });

  it('calls onClick when clicked', () => {
    const onClick = vi.fn();
    render(<Button onClick={onClick}>Click</Button>);
    userEvent.click(screen.getByRole('button'));
    expect(onClick).toHaveBeenCalled();
  });

  it('renders loading state', () => {
    render(<Button isLoading>Loading</Button>);
    expect(screen.getByRole('button')).toHaveAttribute('disabled');
  });

  it('is keyboard accessible', () => {
    const onClick = vi.fn();
    render(<Button onClick={onClick}>Click</Button>);
    userEvent.tab();
    userEvent.keyboard('{Enter}');
    expect(onClick).toHaveBeenCalled();
  });

  it('handles edge case: very long text', () => {
    const longText = 'A'.repeat(100);
    const { container } = render(<Button>{longText}</Button>);
    expect(container.firstChild).toHaveStyle('overflow: hidden');
  });
});
```

**Why:** Prevents regressions. Documents expected behavior. Catches bugs early. Gives confidence for refactoring.

***

#### **J. TYPE SAFETY (TYPESCRIPT MANDATORY)** 🛡️

**Rule:** Use TypeScript for all component code. No `any` types.

```typescript
// ❌ BAD
function Button(props: any) { ... }

// ✅ GOOD
interface ButtonProps {
  children: React.ReactNode;
  onClick: (e: React.MouseEvent<HTMLButtonElement>) => void;
  variant?: 'primary' | 'secondary';
  disabled?: boolean;
}

export const Button: React.FC<ButtonProps> = (props) => { ... }
```

**Benefits:**

- Catches errors at compile time
- IDE suggests correct props
- Self-documenting
- Refactoring is safe
- Prevents prop typos

***

#### **K. VERSION CONTROL \& CHANGELOG** 📖

**Rule:** Every change must be tracked with:

1. **Descriptive commit messages**
2. **CHANGELOG entry**
3. **Migration guide** (if breaking changes)
4. **Version bump** (semantic versioning)
```markdown
## [2.1.0] - 2025-12-20

### Added
- Button component now supports `icon` prop
- New `success` variant for Button

### Changed
- Button default size changed from `md` to `sm`
- Button padding reduced by 4px for compact layout

### Deprecated
- `isLoading` prop (use `state="loading"` instead)

### Fixed
- Button focus outline not visible in dark mode
- Button text truncation on long text

### Breaking Changes
- Removed `type` prop (use `variant` instead)
- Changed `onClick` signature

### Migration Guide
```

<Button type="danger" onClick={(e) => ...}>Delete</Button>

```after
<Button variant="danger" onClick={(e) => ...}>Delete</Button>
\```
```

**Why:** Maintainability. Understanding evolution. Rollback capability. Team communication.

---

#### **L. PERFORMANCE CONSIDERATIONS** ⚡

**Rule:** Components must be optimized for rendering performance.

```
// ✅ GOOD: Memoized to prevent unnecessary re-renders
export const Button = React.memo<ButtonProps>(({
  children,
  onClick,
  variant = 'primary'
}) => {
  return (
    <button
      className={`btn btn--${variant}`}
      onClick={onClick}
    >
      {children}
    </button>
  );
});

// ✅ GOOD: useCallback to preserve function reference
const UserList = ({ users }) => {
  const handleDelete = useCallback((id: number) => {
    // deletion logic
  }, []);

  return users.map(user => (
    <UserItem key={user.id} onDelete={handleDelete} />
  ));
};

// ✅ GOOD: Lazy loading for heavy components
const HeavyChart = React.lazy(() => import('./HeavyChart'));

function Dashboard() {
  return (
    <Suspense fallback={<Skeleton />}>
      <HeavyChart />
    </Suspense>
  );
}
```

**Avoid:**

- ❌ Creating new objects/functions in render
- ❌ Unnecessary component re-renders
- ❌ Missing `key` props in lists
- ❌ Bundle bloat with unused imports

---

#### **M. ERROR BOUNDARIES \& RESILIENCE** 🚨

**Rule:** Components must handle errors gracefully without crashing the entire app.

```
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    console.error('Component error:', error, errorInfo);
    logErrorToService(error);
  }

  render() {
    if (this.state.hasError) {
      return (
        <div role="alert">
          <h2>Something went wrong</h2>
          <details>{this.state.error?.message}</details>
        </div>
      );
    }

    return this.props.children;
  }
}
```

**Also implement:**

- Try-catch for async operations
- Null checks for optional data
- Fallback UI for missing content
- User-friendly error messages (not stack traces)

---

#### **N. STYLE ISOLATION \& CSS-IN-JS** 🎨

**Rule:** Styles must not leak between components. Use CSS Modules, BEM, or CSS-in-JS.

```
// ❌ BAD: Global styles that could conflict
<style>
  .button { padding: 8px; }
</style>

// ✅ GOOD: Scoped styles
// Button.module.css
.button {
  padding: 8px;
  border-radius: 4px;
}

.primary {
  background: blue;
}

// Button.tsx
import styles from './Button.module.css';

export const Button = ({ variant = 'primary', ...props }) => (
  <button className={`${styles.button} ${styles[variant]}`} {...props} />
);

// ✅ ALSO GOOD: CSS-in-JS
import styled from 'styled-components';

const StyledButton = styled.button`
  padding: 8px;
  border-radius: 4px;
  background: ${props => props.variant === 'primary' ? 'blue' : 'gray'};
`;
```


---

#### **O. STORYBOOK/DOCUMENTATION COMPONENTS** 📖

**Rule:** Every component should have a Storybook story demonstrating all states and variants.

```
// Button.stories.tsx
import type { Meta, StoryObj } from '@storybook/react';
import { Button } from './Button';

const meta: Meta<typeof Button> = {
  component: Button,
  tags: ['autodocs'],
  argTypes: {
    variant: {
      control: 'select',
      options: ['primary', 'secondary', 'danger'],
    },
    size: {
      control: 'select',
      options: ['sm', 'md', 'lg'],
    },
  },
};

export default meta;
type Story = StoryObj<typeof meta>;

export const Primary: Story = {
  args: {
    children: 'Button',
    variant: 'primary',
  },
};

export const Loading: Story = {
  args: {
    children: 'Loading...',
    isLoading: true,
  },
};

export const Disabled: Story = {
  args: {
    children: 'Disabled',
    disabled: true,
  },
};

export const AllVariants: Story = {
  render: () => (
    <>
      <Button variant="primary">Primary</Button>
      <Button variant="secondary">Secondary</Button>
      <Button variant="danger">Danger</Button>
    </>
  ),
};
```

**Why:** Visual documentation. Isolated component testing. Design system reference. Stakeholder feedback. Living documentation.

---

### **PART 3: STRUCTURE \& ORGANIZATION** 📁

#### **Recommended File Structure:**

```
src/
├── components/
│   ├── atoms/
│   │   ├── button/
│   │   │   ├── Button.tsx
│   │   │   ├── Button.test.tsx
│   │   │   ├── Button.stories.tsx
│   │   │   ├── Button.module.css
│   │   │   └── Button.types.ts
│   │   ├── input/
│   │   ├── icon/
│   │   └── typography/
│   ├── molecules/
│   │   ├── search-input/
│   │   ├── form-field/
│   │   └── nav-item/
│   ├── organisms/
│   │   ├── header/
│   │   ├── sidebar/
│   │   └── modal/
│   ├── templates/
│   │   ├── dashboard-layout/
│   │   ├── auth-layout/
│   │   └── content-layout/
│   └── index.ts (barrel export)
├── hooks/
│   ├── useAuth.ts
│   ├── useLocalStorage.ts
│   └── index.ts
├── types/
│   ├── common.types.ts
│   └── api.types.ts
├── utils/
│   ├── formatting.ts
│   ├── validation.ts
│   └── index.ts
└── constants/
    └── theme.ts
```


#### **Barrel Exports (index.ts pattern):**

```
// components/atoms/index.ts
export { Button } from './button/Button';
export type { ButtonProps } from './button/Button.types';
export { Input } from './input/Input';
export type { InputProps } from './input/Input.types';

// Usage becomes clean
import { Button, Input } from '@/components/atoms';
```


---

### **PART 4: DOCUMENTATION REQUIREMENTS** 📋

#### **README for Each Component:**

```
# Button Component

## Purpose
Primary interactive element for user actions. Used throughout the application for form submission, navigation, and triggering actions.

## Usage

### Basic
\```tsx
<Button>Click Me</Button>
\```

### With Variants
\```tsx
<Button variant="primary">Primary</Button>
<Button variant="secondary">Secondary</Button>
<Button variant="danger">Delete</Button>
\```

### Disabled State
\```tsx
<Button disabled>Disabled</Button>
\```

### Loading State
\```tsx
<Button isLoading>Processing...</Button>
\```

## Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| children | ReactNode | - | Button content (text or icon) |
| variant | 'primary' \| 'secondary' \| 'danger' | 'primary' | Visual style |
| size | 'sm' \| 'md' \| 'lg' | 'md' | Button size |
| onClick | (e: React.MouseEvent) => void | - | Click handler |
| disabled | boolean | false | Disabled state |
| isLoading | boolean | false | Loading state (shows spinner) |
| type | 'button' \| 'submit' \| 'reset' | 'button' | HTML type attribute |
| fullWidth | boolean | false | Stretch to parent width |
| aria-label | string | - | Accessible label (required if no visible text) |

## Accessibility

- ✅ Keyboard accessible (Tab, Enter, Space)
- ✅ Screen reader compatible
- ✅ Focus outline always visible
- ✅ High contrast in all states

**Important:** Icon-only buttons MUST have `aria-label` prop.

## Variants

### Primary Button
Used for primary actions (submit, save, confirm).

### Secondary Button
Used for secondary actions (cancel, skip, view more).

### Danger Button
Used for destructive actions (delete, remove, clear).

## Related Components

- [Input](../input/Input.md) - Text input field
- [Form](../organisms/form/Form.md) - Complete form component

## Changelog

See [CHANGELOG.md](./CHANGELOG.md)
```


---

### **PART 5: NEVER-FORGET CHECKLIST FOR AI AGENTS** ✅

Print this out. Reference it before writing any component code:

```
ATOMIC DESIGN CHECKLIST
========================

BEFORE CODING:
- [ ] Determined which level (atom/molecule/organism)
- [ ] Checked if it's truly indivisible (atoms) or composite (molecules/organisms)
- [ ] Reviewed existing components to avoid duplication
- [ ] Sketched prop interface on paper
- [ ] Identified all possible states (normal, hover, active, disabled, loading, error, focus)
- [ ] Considered accessibility needs
- [ ] Planned TypeScript types

DURING CODING:
- [ ] Used TypeScript with strict typing (no `any`)
- [ ] Documented all props with JSDoc comments
- [ ] Implemented all documented states
- [ ] Added ARIA labels/roles where needed
- [ ] Used semantic HTML elements (button, input, form, etc.)
- [ ] Avoided hardcoding values (use props for everything)
- [ ] Avoided data fetching (use dependency injection)
- [ ] Made component testable (pure function or predictable state)
- [ ] Used CSS Modules or CSS-in-JS (scoped styles)
- [ ] Applied React.memo if expensive to render
- [ ] No localStorage/sessionStorage usage

TESTING:
- [ ] Unit tests for all props
- [ ] Integration tests for molecule combinations
- [ ] Accessibility tests (keyboard nav, ARIA)
- [ ] Edge case tests (empty/null/long data)
- [ ] Visual regression tests
- [ ] Storybook story for each variant

DOCUMENTATION:
- [ ] JSDoc comments on every prop
- [ ] Usage examples in comments
- [ ] README.md file
- [ ] Storybook stories
- [ ] CHANGELOG.md entry (if updating existing)
- [ ] Migration guide (if breaking changes)

BEFORE MERGING:
- [ ] All tests pass
- [ ] No console errors/warnings
- [ ] Accessibility audit passed
- [ ] Code reviewed by teammate
- [ ] Storybook stories working
- [ ] Documentation updated
- [ ] Naming conventions followed
- [ ] No prop drilling (if 3+ levels deep, restructure)

PERFORMANCE:
- [ ] No unnecessary re-renders
- [ ] No object literals in JSX
- [ ] No functions created in render
- [ ] Memoization applied where needed
- [ ] Bundle size impact assessed

SECURITY:
- [ ] No innerHTML with user content
- [ ] XSS prevention considered
- [ ] Form inputs validated
- [ ] Error messages don't leak sensitive info
```


---

### **PART 6: CRITICAL DON'Ts FOR AI AGENTS** 🚫

Never violate these rules:

1. **❌ NEVER create components without TypeScript**
2. **❌ NEVER use `any` type**
3. **❌ NEVER skip accessibility**
4. **❌ NEVER skip testing**
5. **❌ NEVER hardcode values**
6. **❌ NEVER fetch data in presentational components**
7. **❌ NEVER skip documentation**
8. **❌ NEVER create "god components"** with too many props/responsibilities
9. **❌ NEVER mutate state directly**
10. **❌ NEVER use browser storage (localStorage, sessionStorage)**
11. **❌ NEVER create global CSS that affects multiple components**
12. **❌ NEVER use `innerHTML` with dynamic content**
13. **❌ NEVER skip error handling**
14. **❌ NEVER create components with side effects in the render phase**
15. **❌ NEVER use key={index}** in lists where items can reorder
16. **❌ NEVER skip prop validation**
17. **❌ NEVER ignore TypeScript warnings**
18. **❌ NEVER ship components with console.log() statements**
19. **❌ NEVER forget accessibility in modals, dropdowns, carousels**
20. **❌ NEVER assume data is shaped a certain way** - always validate

---

This comprehensive guide should serve as your reference document for maintaining enterprise-grade component systems. The key is **consistency**, **documentation**, and **never accepting shortcuts**—especially with TypeScript and accessibility.
