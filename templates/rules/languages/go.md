# Go Development Rules

## Modules
- Use Go Modules (`go.mod`).
- Vendor dependencies if required (`go mod vendor`).

## Formatting
- Run `go fmt ./...` before committing.
- Run `go vet ./...` to check for suspicious constructs.

## Testing
- Use standard `testing` package.
- File names: `_test.go`.
- Run tests: `go test -v ./...`.

## Concurrency
- Prefer Channels over Mutexes where possible.
- Handle context cancellation.
