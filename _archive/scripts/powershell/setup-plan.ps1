#!/usr/bin/env pwsh
# Setup implementation plan for a feature

[CmdletBinding()]
param(
    [switch]$Json,
    [switch]$Help
)

$ErrorActionPreference = 'Stop'

# Show help if requested
if ($Help) {
    Write-Output "Usage: ./setup-plan.ps1 [-Json] [-Help]"
    Write-Output "  -Json     Output results in JSON format"
    Write-Output "  -Help     Show this help message"
    exit 0
}

# Load common functions
. "$PSScriptRoot/common.ps1"

# Get all paths and variables from common functions
$paths = Get-FeaturePathsEnv

# Check if we're on a proper feature branch (only for git repos)
if (-not (Test-FeatureBranch -Branch $paths.CURRENT_BRANCH -HasGit $paths.HAS_GIT)) {
    exit 1
}

# Ensure the feature directory exists
New-Item -ItemType Directory -Path $paths.FEATURE_DIR -Force | Out-Null

# Copy plan template if it exists, otherwise note it or create empty file
$template = Join-Path $paths.REPO_ROOT '.specify/templates/plan-template.md'
if (Test-Path $template) {
    Copy-Item $template $paths.IMPL_PLAN -Force
    Write-Output "Copied plan template to $($paths.IMPL_PLAN)"
} else {
    Write-Warning "Plan template not found at $template"
    # Create a basic plan file if template doesn't exist
    New-Item -ItemType File -Path $paths.IMPL_PLAN -Force | Out-Null
}

# Prompt for IA MAX fields if missing (interactive only)
if (-not $Json) {
    $needsOrch = -not (Select-String -Path $paths.IMPL_PLAN -Pattern '^\*\*Orchestration\*\*:' -Quiet)
    $needsMem  = -not (Select-String -Path $paths.IMPL_PLAN -Pattern '^\*\*Shared Memory\*\*:' -Quiet)

    $orchToWrite = $null
    $memToWrite = $null

    if ($needsOrch) {
        $orch = Read-Host "Choose Orchestration [Agno/ADK/Letta] (default: Agno)"
        switch -Regex ($orch) {
            '^\s*(ADK)\s*$'   { $orchToWrite = 'ADK' }
            '^\s*(Letta)\s*$' { $orchToWrite = 'Letta' }
            default           { $orchToWrite = 'Agno' }
        }
    }
    if ($needsMem) {
        $mem = Read-Host "Choose Shared Memory [Graphiti/MemFuse/Cognee/Mem0] (default: Graphiti)"
        switch -Regex ($mem) {
            '^\s*(MemFuse)\s*$' { $memToWrite = 'MemFuse' }
            '^\s*(Cognee)\s*$'  { $memToWrite = 'Cognee' }
            '^\s*(Mem0)\s*$'    { $memToWrite = 'Mem0' }
            default             { $memToWrite = 'Graphiti' }
        }
    }

    if ($orchToWrite -or $memToWrite) {
        $hasHeader = Select-String -Path $paths.IMPL_PLAN -Pattern '^### IA MAX Extensions' -Quiet
        if (-not $hasHeader) {
            Add-Content -LiteralPath $paths.IMPL_PLAN -Value ""
            Add-Content -LiteralPath $paths.IMPL_PLAN -Value "### IA MAX Extensions (Parseable Fields)"
            Add-Content -LiteralPath $paths.IMPL_PLAN -Value ""
        }
        if ($orchToWrite) { Add-Content -LiteralPath $paths.IMPL_PLAN -Value "- **Orchestration**: $orchToWrite" }
        if ($memToWrite)  { Add-Content -LiteralPath $paths.IMPL_PLAN -Value "- **Shared Memory**: $memToWrite" }
        Write-Output "Updated IA MAX fields in $($paths.IMPL_PLAN)"
    }
}

# Output results
if ($Json) {
    $result = [PSCustomObject]@{
        FEATURE_SPEC = $paths.FEATURE_SPEC
        IMPL_PLAN = $paths.IMPL_PLAN
        SPECS_DIR = $paths.FEATURE_DIR
        BRANCH = $paths.CURRENT_BRANCH
        HAS_GIT = $paths.HAS_GIT
    }
    $result | ConvertTo-Json -Compress
} else {
    Write-Output "FEATURE_SPEC: $($paths.FEATURE_SPEC)"
    Write-Output "IMPL_PLAN: $($paths.IMPL_PLAN)"
    Write-Output "SPECS_DIR: $($paths.FEATURE_DIR)"
    Write-Output "BRANCH: $($paths.CURRENT_BRANCH)"
    Write-Output "HAS_GIT: $($paths.HAS_GIT)"
}
