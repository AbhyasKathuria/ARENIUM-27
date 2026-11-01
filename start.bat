@echo off
setlocal
title ARENIUM '27 - Tech Fest Portal
cd /d "%~dp0"

echo ====================================================================
echo   [+] ARENIUM '27 // SCHOOL OF INFORMATION SCIENCE
echo   [+] PRESIDENCY UNIVERSITY, BENGALURU
echo   [+] CYBERPUNK TECH FEST PORTAL
echo ====================================================================
echo.

:: 1. Check Python
where python >nul 2>&1
if %ERRORLEVEL% equ 0 (
    set "RUNNER=python"
    goto :run_python
)

:: 2. Check py launcher
where py >nul 2>&1
if %ERRORLEVEL% equ 0 (
    set "RUNNER=py"
    goto :run_python
)

:: 3. Check Node.js / npx
where npx >nul 2>&1
if %ERRORLEVEL% equ 0 (
    echo [*] Python not found, Node.js detected.
    echo [*] Starting local server via npx serve...
    start "" "http://localhost:3000"
    npx --yes serve -l 3000 "%~dp0"
    goto :done
)

:: 4. Fallback: Open index.html directly in default browser
echo [!] Python or Node.js was not detected in PATH.
echo [*] Launching ARENIUM '27 directly in your default browser...
start "" "%~dp0index.html"
goto :done

:run_python
echo [*] Starting local HTTP server...
%RUNNER% -c "import http.server, socketserver, webbrowser, threading, socket; s=socket.socket; p=next(port for port in range(8000, 8050) if s().connect_ex(('127.0.0.1', port)) != 0); threading.Timer(0.8, lambda: webbrowser.open('http://localhost:' + str(p))).start(); print('\n  [+] ARENIUM 27 is live at: http://localhost:' + str(p)); print('  [+] Default browser opened automatically.'); print('  [!] Press Ctrl+C in this window to stop the server.\n'); socketserver.TCPServer.allow_reuse_address = True; httpd = socketserver.TCPServer(('', p), http.server.SimpleHTTPRequestHandler); httpd.serve_forever()"
goto :done

:done
pause
