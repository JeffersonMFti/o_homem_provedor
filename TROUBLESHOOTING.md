# Troubleshooting - Problemas Comuns

## Os dados não aparecem na página web

### Problema: Abrir HTML diretamente do sistema de arquivos

**Sintoma:** Você abriu o arquivo `web/index.html` diretamente no navegador (URL começa com `file://`) e os gráficos não aparecem.

**Causa:** Navegadores modernos bloqueiam requisições AJAX/fetch quando a página é servida diretamente do sistema de arquivos por questões de segurança (CORS policy).

**Solução:**

1. **Use o servidor HTTP local:**
   ```bash
   python serve_web.py
   ```
   Depois acesse: http://localhost:8000

2. **Ou use qualquer servidor HTTP simples:**
   ```bash
   # Python 3
   cd web
   python -m http.server 8000
   
   # Node.js (se tiver npx instalado)
   cd web
   npx serve
   ```

### Problema: Arquivos JSON não existem

**Sintoma:** Console do navegador mostra erros 404 ao tentar carregar arquivos `.json`.

**Causa:** Os dados ainda não foram gerados pelo pipeline.

**Solução:**
```bash
python run_pipeline.py
```

Isso vai gerar os arquivos:
- `web/data/funil_nacional.json`
- `web/data/funil_por_estado.json`  
- `web/data/distribuicao_renda.json`
- `web/data/razao_por_uf.json`

### Problema: Erro ao executar run_pipeline.py

**Sintoma:** `ModuleNotFoundError` ou erros de import.

**Solução:**
1. Certifique-se de que o ambiente virtual está ativado:
   ```bash
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

### Problema: Porta 8000 já em uso

**Sintoma:** Ao executar `serve_web.py`, aparece erro `[WinError 10048]` ou similar.

**Causa:** Outra aplicação está usando a porta 8000, ou o servidor já está rodando.

**Solução:**
1. Verifique se o servidor já está rodando e acesse http://localhost:8000
2. Ou edite `serve_web.py` e mude `PORT = 8000` para outro número (ex: `PORT = 8080`)

## Verificar se os dados foram gerados corretamente

Execute:
```bash
python -c "import json; print(json.load(open('web/data/funil_nacional.json')))"
```

Você deve ver algo como:
```json
{
  "ano_referencia": 2022,
  "renda_minima": 10000,
  "homens_empregados": 49668511,
  "homens_10k": 2568061,
  ...
}
```

## Console do navegador

Para investigar erros, abra o Console do navegador:
- **Chrome/Edge:** F12 ou Ctrl+Shift+I → aba "Console"
- **Firefox:** F12 ou Ctrl+Shift+I → aba "Console"

Procure por mensagens de erro em vermelho. As mais comuns:
- `net::ERR_FAILED` → problema ao carregar arquivo (verifique se serve_web.py está rodando)
- `CORS policy` → está abrindo o HTML diretamente (use serve_web.py)
- `404 Not Found` → arquivo JSON não existe (execute run_pipeline.py)

## Deploy no Vercel

Se hospedado no Vercel e os dados não aparecem:

1. Verifique se os arquivos JSON estão no repositório Git:
   ```bash
   git add web/data/*.json
   git commit -m "Add data files"
   git push
   ```

2. Force um novo deploy no Vercel

3. Verifique os logs de build no painel do Vercel

## Ainda com problemas?

1. Verifique se todos os arquivos existem:
   - `web/index.html`
   - `web/main.js`
   - `web/style.css`
   - `web/data/funil_nacional.json`
   - `web/data/funil_por_estado.json`
   - `web/data/distribuicao_renda.json`
   - `web/data/razao_por_uf.json`

2. Teste o servidor local:
   ```bash
   python serve_web.py
   ```
   Acesse http://localhost:8000 e abra o console do navegador (F12)

3. Verifique se há mensagens de erro no console
