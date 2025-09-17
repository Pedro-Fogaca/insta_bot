@echo off
cd C:\Users\Administrador\Documents\insta_bot
call venv\Scripts\activate.bat
:loop
python bot_instagrapi.py
timeout /t 5
goto loop
