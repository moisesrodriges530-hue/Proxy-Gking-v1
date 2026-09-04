@echo off
REM Script de compilacao automatica - Windows
REM Proxy Gking v1

echo [+] Proxy Gking v1 - Compilador Automatico
echo [+] Instalando dependencias...

pip install buildozer cython kivy requests colorama

echo [+] Compilando APK (DEBUG)...
buildozer android debug

echo [+] APK compilado!
echo [+] Localizacao: bin\proxygking-1.0-debug.apk
echo [+] Instale com: adb install bin\proxygking-1.0-debug.apk

pause