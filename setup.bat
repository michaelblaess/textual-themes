@echo off
setlocal

set REPO=%~dp0
set VENV=%REPO%.venv

if not exist "%VENV%" (
    echo Creating virtual environment...
    python -m venv "%VENV%"
    if errorlevel 1 (
        echo Failed to create venv. Is Python 3.12+ installed and on PATH?
        exit /b 1
    )
)

REM Zscaler / corporate proxy workaround: pip.ini applies to all pip subprocesses,
REM including the isolated build environments that pick up setuptools.
set PIP_TRUSTED=--trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org
if not exist "%VENV%\pip.ini" (
    echo [global]> "%VENV%\pip.ini"
    echo trusted-host = pypi.org pypi.python.org files.pythonhosted.org>> "%VENV%\pip.ini"
)

echo Upgrading pip...
"%VENV%\Scripts\python.exe" -m pip install --upgrade pip --quiet %PIP_TRUSTED%
if errorlevel 1 exit /b 1

echo Installing textual-themes (editable)...
"%VENV%\Scripts\pip.exe" install -e "%REPO%." --quiet %PIP_TRUSTED%
if errorlevel 1 exit /b 1

echo.
echo Setup complete.
echo.
echo Run the demo:
echo     "%VENV%\Scripts\python.exe" -m textual_themes
echo.
echo List available themes:
echo     "%VENV%\Scripts\python.exe" -m textual_themes --list
