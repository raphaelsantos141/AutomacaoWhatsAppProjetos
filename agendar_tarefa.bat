@echo off
set NOME_TAREFA=AutomacaoWhatsApp
set HORA=06:50
set SCRIPT_PATH=C:\AutomacaoWhatsApp\send_whatsapp_edge.py
set PYTHON_PATH=C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python312\python.exe

schtasks /create ^
 /tn "%NOME_TAREFA%" ^
 /tr "\"%PYTHON_PATH%\" \"%SCRIPT_PATH%\"" ^
 /sc daily ^
 /st %HORA% ^
 /rl highest ^
 /f

echo Tarefa %NOME_TAREFA% criada com sucesso para rodar diariamente às %HORA%.
pause

@echo off
set NOME_TAREFA=AutomacaoWhatsApp8Hrs
set HORA=08:00
set SCRIPT_PATH=C:\AutomacaoWhatsApp\send_whatsapp_edge.py
set PYTHON_PATH=C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python312\python.exe

schtasks /create ^
 /tn "%NOME_TAREFA%" ^
 /tr "\"%PYTHON_PATH%\" \"%SCRIPT_PATH%\"" ^
 /sc daily ^
 /st %HORA% ^
 /rl highest ^
 /f

echo Tarefa %NOME_TAREFA% criada com sucesso para rodar diariamente às %HORA%.
pause
