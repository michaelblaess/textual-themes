#Requires -Version 5.1
<#
.SYNOPSIS
    Sets up the textual-themes development environment.

.DESCRIPTION
    Creates the .venv via uv, installs runtime + dev dependencies and the
    Nuitka build tool (for compile-win64.ps1). Run once after cloning the repo.

    textual-themes is primarily a library; the Nuitka build targets the
    bundled storybook demo app (textual-themes-demo).
#>

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

Write-Host "=== textual-themes - dev environment ===" -ForegroundColor Cyan

Write-Host "[1/2] venv + dependencies (uv sync)..."
uv sync --extra dev
if ($LASTEXITCODE -ne 0) { throw "uv sync fehlgeschlagen" }

Write-Host "[2/2] Nuitka build tool..."
uv pip install nuitka
if ($LASTEXITCODE -ne 0) { throw "nuitka-Installation fehlgeschlagen" }

Write-Host ""
Write-Host "Done. Start with: .\run.ps1" -ForegroundColor Green
