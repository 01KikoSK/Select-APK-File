@echo off
setlocal enabledelayedexpansion

REM Change directory to where APKs are stored
cd /d "C:\path\to\apk\files"

REM List all APK files
echo List of APK files in the directory:
echo -------------------------------
for %%f in (*.apk) do (
    echo %%f
)

REM Prompt user for input
set /p fileName="Enter the name of the APK file to select: "

REM Check if file exists
if exist "%fileName%" (
    echo File found: %fileName%
    REM Perform actions (e.g., move, copy, install simulation)
    echo Performing actions on %fileName%...
    REM Example action: copy to another folder
    copy "%fileName%" "C:\destination\folder"
    echo File copied successfully.
) else (
    echo File not found. Please check the name and try again.
)

pause