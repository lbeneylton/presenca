@echo off
title Instalador do Servidor FastAPI

echo ===============================
echo   INICIANDO INSTALACAO
echo ===============================

REM Verifica Python
python --version >nul 2>&1
if errorlevel 1 (
    echo Python nao encontrado! Instale o Python primeiro.
    pause
    exit /b
)

REM Cria ambiente virtual
echo.
echo [1/5] Criando ambiente virtual...
python -m venv .venv
if errorlevel 1 (
    echo Erro ao criar ambiente virtual!
    pause
    exit /b
)

REM Ativa ambiente
echo.
echo [2/5] Ativando ambiente virtual...
call .venv\Scripts\activate

REM Atualiza pip
echo.
echo [3/5] Atualizando pip...
python -m pip install --upgrade pip

REM Instala dependencias
echo.
echo [4/5] Instalando dependencias...
if not exist requirements.txt (
    echo Arquivo requirements.txt nao encontrado!
    pause
    exit /b
)
pip install -r requirements.txt

REM Verifica app
echo.
echo [5/5] Validando estrutura...
if not exist app (
    echo Pasta "app" nao encontrada!
    pause
    exit /b
)

if not exist app\main.py (
    echo Arquivo main.py nao encontrado dentro de /app!
    pause
    exit /b
)

echo.
echo ===============================
echo   INSTALACAO CONCLUIDA
echo ===============================

REM Menu simples
:menu
echo.
echo Escolha uma opcao:
echo 1 - Iniciar servidor
echo 2 - Sair
set /p op=

if "%op%"=="1" goto start
if "%op%"=="2" exit

goto menu

:start
cd app
echo Iniciando servidor...
uvicorn main:app --host 0.0.0.0 --port 5000 --reload
pause