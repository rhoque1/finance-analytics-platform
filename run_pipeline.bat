@echo off
echo ===================================================
echo     FINANCE ANALYTICS PIPELINE AUTOMATION
echo ===================================================
echo.

echo [1/2] Running Data Transformations (transform.py)...
call venv\Scripts\python.exe transform.py
if %ERRORLEVEL% neq 0 (
    echo.
    echo [ERROR] Transformation failed! Check the code.
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo [2/2] Loading SQL Database (load_database.py)...
call venv\Scripts\python.exe load_database.py
if %ERRORLEVEL% neq 0 (
    echo.
    echo [ERROR] Database load failed! Check the code.
    pause
    exit /b %ERRORLEVEL%
)

echo.
echo ===================================================
echo   SUCCESS! Pipeline complete. Power BI is ready.
echo ===================================================
pause