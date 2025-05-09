@echo off
echo Stopping all instances of 'displanger'...

REM Find all processes with the name 'displanger' and terminate them
for /f "tokens=2 delims=," %%P in ('tasklist /FI "IMAGENAME eq displanger.exe" /FO CSV /NH') do (
    taskkill /PID %%~P /F >nul 2>&1
    echo Terminated process with PID %%~P
)

echo All instances of 'displanger' have been stopped.