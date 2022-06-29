for /r ./apps/ %%i in (*.apk) do ( 
echo %i:~1,-4%
@REM echo %%i >> test.txt
@REM apktool d %%i
@REM findstr /s safetynet %%i/*.smali >> test.txt
)