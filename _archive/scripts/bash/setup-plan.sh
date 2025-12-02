#!/usr/bin/env bash

set -e

# Parse command line arguments
JSON_MODE=false
ARGS=()

for arg in "$@"; do
    case "$arg" in
        --json)
            JSON_MODE=true
            ;;
        --help|-h)
            echo "Usage: $0 [--json]"
            echo "  --json    Output results in JSON format"
            echo "  --help    Show this help message"
            exit 0
            ;;
        *)
            ARGS+=("$arg")
            ;;
    esac
done

# Get script directory and load common functions
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "$SCRIPT_DIR/common.sh"

# Get all paths and variables from common functions
eval $(get_feature_paths)

# Check if we're on a proper feature branch (only for git repos)
check_feature_branch "$CURRENT_BRANCH" "$HAS_GIT" || exit 1

# Ensure the feature directory exists
mkdir -p "$FEATURE_DIR"

# Copy plan template if it exists
TEMPLATE="$REPO_ROOT/.specify/templates/plan-template.md"
if [[ -f "$TEMPLATE" ]]; then
    cp "$TEMPLATE" "$IMPL_PLAN"
    echo "Copied plan template to $IMPL_PLAN"
else
    echo "Warning: Plan template not found at $TEMPLATE"
    # Create a basic plan file if template doesn't exist
    touch "$IMPL_PLAN"
fi

# Prompt for IA MAX fields if missing (interactive mode only)
if ! $JSON_MODE; then
    ORCH_TO_WRITE=""
    MEM_TO_WRITE=""

    # Orchestration
    if ! grep -q '^\*\*Orchestration\*\*:' "$IMPL_PLAN"; then
        read -r -p "Choose Orchestration [Agno/ADK/Letta] (default: Agno): " ORCH
        case "$ORCH" in
            ADK|adk) ORCH_TO_WRITE="ADK" ;;
            Letta|letta) ORCH_TO_WRITE="Letta" ;;
            ""|Agno|agno|AGNO) ORCH_TO_WRITE="Agno" ;;
            *) ORCH_TO_WRITE="Agno" ;;
        esac
    fi

    # Shared Memory
    if ! grep -q '^\*\*Shared Memory\*\*:' "$IMPL_PLAN"; then
        read -r -p "Choose Shared Memory [Graphiti/MemFuse/Cognee/Mem0] (default: Graphiti): " MEM
        case "$MEM" in
            MemFuse|memfuse) MEM_TO_WRITE="MemFuse" ;;
            Cognee|cognee) MEM_TO_WRITE="Cognee" ;;
            Mem0|mem0) MEM_TO_WRITE="Mem0" ;;
            ""|Graphiti|graphiti|GRAPHITI) MEM_TO_WRITE="Graphiti" ;;
            *) MEM_TO_WRITE="Graphiti" ;;
        esac
    fi

    # Append missing fields under IA MAX Extensions if needed
    if [[ -n "$ORCH_TO_WRITE" || -n "$MEM_TO_WRITE" ]]; then
        if ! grep -q '^### IA MAX Extensions' "$IMPL_PLAN"; then
            {
                echo ""
                echo "### IA MAX Extensions (Parseable Fields)"
                echo ""
            } >> "$IMPL_PLAN"
        fi
        [[ -n "$ORCH_TO_WRITE" ]] && echo "- **Orchestration**: $ORCH_TO_WRITE" >> "$IMPL_PLAN"
        [[ -n "$MEM_TO_WRITE" ]] && echo "- **Shared Memory**: $MEM_TO_WRITE" >> "$IMPL_PLAN"
        echo "Updated IA MAX fields in $IMPL_PLAN"
    fi
fi

# Output results
if $JSON_MODE; then
    printf '{"FEATURE_SPEC":"%s","IMPL_PLAN":"%s","SPECS_DIR":"%s","BRANCH":"%s","HAS_GIT":"%s"}\n' \
        "$FEATURE_SPEC" "$IMPL_PLAN" "$FEATURE_DIR" "$CURRENT_BRANCH" "$HAS_GIT"
else
    echo "FEATURE_SPEC: $FEATURE_SPEC"
    echo "IMPL_PLAN: $IMPL_PLAN"
    echo "SPECS_DIR: $FEATURE_DIR"
    echo "BRANCH: $CURRENT_BRANCH"
    echo "HAS_GIT: $HAS_GIT"
fi
