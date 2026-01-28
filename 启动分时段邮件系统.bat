@echo off
chcp 65001 >nul
title 分时段学习任务邮件发送系统

echo.
echo ========================================
echo   分时段学习任务邮件发送系统
echo ========================================
echo.

REM 检查Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python not found!
    pause
    exit /b 1
)

echo [OK] Python installed
echo.

REM 检查依赖
python -c "import docx, schedule" >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing dependencies...
    pip install python-docx schedule
)

echo [OK] Dependencies ready
echo.
echo Starting program...
echo.

REM 运行程序
python daily_study_mailer_advanced.py

pause

