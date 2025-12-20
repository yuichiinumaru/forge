# Java Development Rules

## Build System
- Prefer **Gradle** (Kotlin DSL) or **Maven**.
- Always include a wrapper (`gradlew` or `mvnw`).

## Testing
- Framework: **JUnit 5**.
- Mocking: **Mockito**.
- Run tests: `./gradlew test` or `mvn test`.

## Style & Naming
- Class names: `PascalCase`.
- Methods/Variables: `camelCase`.
- Constants: `UPPER_SNAKE_CASE`.
- Follow Google Java Style Guide.

## Documentation
- Javadoc required for all public classes and interfaces.
