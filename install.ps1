# textual-themes storybook - one-line installer (Windows)
#
#   irm https://raw.githubusercontent.com/michaelblaess/textual-themes/main/install.ps1 | iex
#
# Installs the theme storybook into an isolated venv under
# %LOCALAPPDATA%\textual-themes and puts a `textual-themes-demo`
# launcher on the user PATH.
$ErrorActionPreference = "Stop"

$RepoUrl    = "git+https://github.com/michaelblaess/textual-themes.git"
$InstallDir = Join-Path $env:LOCALAPPDATA "textual-themes"
$Venv       = Join-Path $InstallDir "venv"
$BinDir     = Join-Path $InstallDir "bin"
$Launcher   = Join-Path $BinDir "textual-themes-demo.cmd"

Write-Host "Installing the textual-themes storybook..."

# 1. Locate a Python 3.12+ interpreter.
$pythonBin = $null
foreach ($cand in @("python", "python3", "py")) {
    if (-not (Get-Command $cand -ErrorAction SilentlyContinue)) { continue }
    try {
        $ver = (& $cand -c "import sys; print('%d.%d' % sys.version_info[:2])").Trim()
    } catch { continue }
    $parts = $ver.Split(".")
    if ([int]$parts[0] -eq 3 -and [int]$parts[1] -ge 12) {
        $pythonBin = $cand
        break
    }
}
if ($null -eq $pythonBin) {
    Write-Error "Python 3.12+ is required but was not found on PATH."
    return
}
if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Error "git is required to install from GitHub."
    return
}
Write-Host "Using $(& $pythonBin --version)"

# 2. Create the isolated environment.
New-Item -ItemType Directory -Force -Path $InstallDir | Out-Null
if (-not (Test-Path $Venv)) {
    & $pythonBin -m venv $Venv
}
$VenvPython = Join-Path $Venv "Scripts\python.exe"

# 3. Install / update the package.
& $VenvPython -m pip install --upgrade pip --quiet
& $VenvPython -m pip install --upgrade $RepoUrl --quiet

# 4. Put a launcher on the user PATH.
New-Item -ItemType Directory -Force -Path $BinDir | Out-Null
$demoExe = Join-Path $Venv "Scripts\textual-themes-demo.exe"
"@echo off`r`n`"$demoExe`" %*" | Set-Content -Path $Launcher -Encoding ASCII

$userPath = [Environment]::GetEnvironmentVariable("Path", "User")
if ($userPath -notlike "*$BinDir*") {
    [Environment]::SetEnvironmentVariable("Path", "$userPath;$BinDir", "User")
    Write-Host "Added $BinDir to your user PATH."
}

Write-Host ""
Write-Host "Done. Restart your terminal, then launch the storybook with:"
Write-Host "    textual-themes-demo"
