@echo off
echo 🔄 Deleting all __pycache__ folders and .pyc files...

REM Delete all __pycache__ folders
for /d /r %%d in (__pycache__) do (
    echo Deleting folder: %%d
    rd /s /q "%%d"
)

REM Delete all .pyc files
for /r %%f in (*.pyc) do (
    echo Deleting file: %%f
    del /q "%%f"
)

echo ✅ Done!
pause
