@echo off
setlocal

set VENV_PYTHON=%~dp0.venv\Scripts\python.exe

if exist "%VENV_PYTHON%" (
    "%VENV_PYTHON%" -m textual_themes %*
) else (
    python -m textual_themes %*
)
