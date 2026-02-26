@echo off
REM Script para verificar e iniciar a aplicação web
REM Use: verificar_web.bat

echo ==========================================================
echo Verificando configuração da aplicação web
echo ==========================================================
echo.

REM Verifica se Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Python não encontrado. Instale o Python 3.8+ primeiro.
    pause
    exit /b 1
)
echo [OK] Python instalado

REM Verifica se a pasta web existe
if not exist "web" (
    echo [ERRO] Pasta "web" não encontrada. Execute este script da raiz do projeto.
    pause
    exit /b 1
)
echo [OK] Pasta web encontrada

REM Verifica se os arquivos principais existem
if not exist "web\index.html" (
    echo [ERRO] web\index.html não encontrado
    pause
    exit /b 1
)
echo [OK] index.html encontrado

if not exist "web\main.js" (
    echo [ERRO] web\main.js não encontrado
    pause
    exit /b 1
)
echo [OK] main.js encontrado

REM Verifica se a pasta de dados existe
if not exist "web\data" (
    echo [AVISO] Pasta web\data não encontrada. Criando...
    mkdir "web\data"
)
echo [OK] Pasta web\data existe

REM Verifica se os arquivos JSON existem
set MISSING=0
echo.
echo Verificando arquivos de dados JSON:

if not exist "web\data\funil_nacional.json" (
    echo   [X] funil_nacional.json - FALTANDO
    set MISSING=1
) else (
    echo   [OK] funil_nacional.json
)

if not exist "web\data\funil_por_estado.json" (
    echo   [X] funil_por_estado.json - FALTANDO
    set MISSING=1
) else (
    echo   [OK] funil_por_estado.json
)

if not exist "web\data\distribuicao_renda.json" (
    echo   [X] distribuicao_renda.json - FALTANDO
    set MISSING=1
) else (
    echo   [OK] distribuicao_renda.json
)

if not exist "web\data\razao_por_uf.json" (
    echo   [X] razao_por_uf.json - FALTANDO
    set MISSING=1
) else (
    echo   [OK] razao_por_uf.json
)

echo.
if %MISSING%==1 (
    echo [AVISO] Alguns arquivos JSON estão faltando.
    echo.
    echo Deseja gerar os dados agora? (Isso pode levar alguns minutos)
    choice /C SN /M "Executar 'python run_pipeline.py'"
    if errorlevel 2 goto :start_server
    if errorlevel 1 (
        echo.
        echo Executando pipeline...
        python run_pipeline.py
        if errorlevel 1 (
            echo [ERRO] Falha ao executar pipeline
            pause
            exit /b 1
        )
        echo [OK] Dados gerados com sucesso
    )
)

:start_server
echo.
echo ==========================================================
echo Iniciando servidor web...
echo ==========================================================
echo.
echo O servidor vai iniciar na porta 8000
echo Acesse: http://localhost:8000
echo.
echo Pressione Ctrl+C para parar o servidor
echo.
pause

python serve_web.py

pause
