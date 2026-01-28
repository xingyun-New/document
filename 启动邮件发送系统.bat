@echo off
chcp 65001 >nul
title 每日学习计划自动邮件发送系统

echo.
echo ========================================
echo   每日学习计划自动邮件发送系统
echo ========================================
echo.

REM 检查Python是否安装
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ 错误：未检测到Python！
    echo 请先安装Python 3.6或更高版本
    echo 下载地址：https://www.python.org/downloads/
    pause
    exit /b 1
)

echo ✅ Python已安装
echo.

REM 检查依赖包
echo 正在检查依赖包...
python -c "import docx, schedule" >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo ⚠️  检测到缺少依赖包，正在自动安装...
    echo.
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo.
        echo ❌ 依赖包安装失败！
        echo 请手动运行：pip install python-docx schedule
        pause
        exit /b 1
    )
    echo.
    echo ✅ 依赖包安装完成！
)

echo ✅ 依赖包检查完成
echo.
echo 正在启动程序...
echo.

REM 运行主程序
python daily_study_mailer.py

pause

