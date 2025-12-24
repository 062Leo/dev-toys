@echo off
setlocal

:: Get the directory where this batch file is located
set "SCRIPT_DIR=%~dp0"
set "PROJECT_ROOT=%SCRIPT_DIR%.."

:: Navigate to project root
cd /d "%PROJECT_ROOT%"

:: Run the Python script silently
python "%SCRIPT_DIR%generate_readme.py" >nul 2>&1

:: Check if Python script ran successfully
if %ERRORLEVEL% EQU 0 (
    echo README.md has been updated successfully.
) else (
    echo Error: Failed to update README.md
    pause
    exit /b 1
)

exit /b 0
