# Domain Aggregate: [Aggregate Name]

**Domain**: [Domain Name]
**Root Entity**: [Entity Name]

## 1. Description
*What does this aggregate represent? What is its boundary?*
- Example: "A Game Match representing the state of a chess game between two players."

## 2. Invariants (Business Rules)
*Rules that must ALWAYS be consistent within this aggregate.*
- [ ] **Rule 1**: [Description] (e.g., "A player cannot play against themselves.")
- [ ] **Rule 2**: [Description] (e.g., "Game cannot start with < 2 players.")

## 3. State Transitions
*Valid states and transitions.*
- `Draft` -> `Started`
- `Started` -> `Finished`

## 4. Child Entities & Value Objects
*Components managed by this aggregate.*
- **Entities**: ...
- **Value Objects**: ...

## 5. Commands / Methods
*Public API of the aggregate.*
- `startGame()`
- `makeMove(move)`
