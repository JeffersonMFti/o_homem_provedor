#!/bin/bash
# Script para verificar e iniciar a aplicação web
# Use: bash verificar_web.sh ou ./verificar_web.sh

echo "=========================================================="
echo "Verificando configuração da aplicação web"
echo "=========================================================="
echo ""

# Verifica se Python está instalado
if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null
then
    echo "[ERRO] Python não encontrado. Instale o Python 3.8+ primeiro."
    exit 1
fi
echo "[OK] Python instalado"

# Define o comando Python
PYTHON_CMD="python3"
if ! command -v python3 &> /dev/null; then
    PYTHON_CMD="python"
fi

# Verifica se a pasta web existe
if [ ! -d "web" ]; then
    echo "[ERRO] Pasta 'web' não encontrada. Execute este script da raiz do projeto."
    exit 1
fi
echo "[OK] Pasta web encontrada"

# Verifica se os arquivos principais existem
if [ ! -f "web/index.html" ]; then
    echo "[ERRO] web/index.html não encontrado"
    exit 1
fi
echo "[OK] index.html encontrado"

if [ ! -f "web/main.js" ]; then
    echo "[ERRO] web/main.js não encontrado"
    exit 1
fi
echo "[OK] main.js encontrado"

# Verifica se a pasta de dados existe
if [ ! -d "web/data" ]; then
    echo "[AVISO] Pasta web/data não encontrada. Criando..."
    mkdir -p "web/data"
fi
echo "[OK] Pasta web/data existe"

# Verifica se os arquivos JSON existem
MISSING=0
echo ""
echo "Verificando arquivos de dados JSON:"

FILES=("funil_nacional.json" "funil_por_estado.json" "distribuicao_renda.json" "razao_por_uf.json")
for FILE in "${FILES[@]}"; do
    if [ ! -f "web/data/$FILE" ]; then
        echo "  [X] $FILE - FALTANDO"
        MISSING=1
    else
        echo "  [OK] $FILE"
    fi
done

echo ""
if [ $MISSING -eq 1 ]; then
    echo "[AVISO] Alguns arquivos JSON estão faltando."
    echo ""
    read -p "Deseja gerar os dados agora? (s/n) " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[SsYy]$ ]]; then
        echo ""
        echo "Executando pipeline..."
        $PYTHON_CMD run_pipeline.py
        if [ $? -ne 0 ]; then
            echo "[ERRO] Falha ao executar pipeline"
            exit 1
        fi
        echo "[OK] Dados gerados com sucesso"
    fi
fi

echo ""
echo "=========================================================="
echo "Iniciando servidor web..."
echo "=========================================================="
echo ""
echo "O servidor vai iniciar na porta 8000"
echo "Acesse: http://localhost:8000"
echo ""
echo "Pressione Ctrl+C para parar o servidor"
echo ""

$PYTHON_CMD serve_web.py
