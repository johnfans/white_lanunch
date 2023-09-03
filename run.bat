@echo
setlocal

:: 获取当前批处理文件所在的目录
set "CURRENT_DIR=%~dp0"

:: 设置工作目录为当前批处理文件所在的目录
cd /d "%CURRENT_DIR%"

:: 在当前目录下执行 test.py
python main2.py

endlocal