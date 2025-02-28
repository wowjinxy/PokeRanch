@echo off
setlocal

echo Configuring for WBME_1...
python configure.py
if %errorlevel% neq 0 (
    echo Failed to configure WBME_1. Exiting...
    pause
    exit /b %errorlevel%
)

echo Building WBME_1...
ninja
if %errorlevel% neq 0 (
    echo Failed to build WBME_1. Exiting...
    pause
    exit /b %errorlevel%
)

echo Configuring for WBMJ_258...
python configure.py --version WBMJ_258
if %errorlevel% neq 0 (
    echo Failed to configure WBMJ_258. Exiting...
    pause
    exit /b %errorlevel%
)

echo Building WBMJ_258...
ninja
if %errorlevel% neq 0 (
    echo Failed to build WBMJ_258. Exiting...
    pause
    exit /b %errorlevel%
)

echo All builds completed successfully.
pause
exit /b 0
