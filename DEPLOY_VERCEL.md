# 🚀 Deploy no Vercel — Landing Page React

## 📋 Pré-requisitos

1. **Conta no Vercel** (gratuita): [vercel.com/signup](https://vercel.com/signup)
2. **Vercel CLI** instalado (opcional, mas recomendado)

## 🎯 Método 1: Deploy via GitHub (Recomendado)

### Passo 1: Commit e Push

```bash
# Adicionar todos os arquivos novos
git add .

# Criar commit
git commit -m "feat: adiciona landing page React premium"

# Push para o GitHub
git push origin main
```

### Passo 2: Deploy no Vercel

1. Acesse [vercel.com/new](https://vercel.com/new)
2. **Import Git Repository**
3. Selecione o repositório `o_homem_provedor`
4. Configure o projeto:

**Framework Preset:** Vite  
**Root Directory:** `./` (raiz do projeto)  
**Build Command:** `cd web && npm install && npm run build`  
**Output Directory:** `web/dist`  
**Install Command:** `cd web && npm install`

5. Clique em **Deploy**

### Passo 3: Aguarde o Build

O Vercel vai:
- Instalar dependências (`npm install`)
- Executar build do Vite (`npm run build`)
- Fazer deploy do conteúdo da pasta `web/dist/`

**Tempo estimado:** 2-3 minutos

---

## 🎯 Método 2: Deploy via Vercel CLI

### Instalação da CLI

```bash
npm install -g vercel
```

### Login

```bash
vercel login
```

### Deploy

```bash
# Na raiz do projeto
vercel

# Ou deploy direto para produção
vercel --prod
```

A CLI vai usar automaticamente as configurações do `vercel.json`.

---

## 📁 Arquivos de Configuração

### vercel.json (já configurado ✅)

```json
{
  "buildCommand": "cd web && npm install && npm run build",
  "outputDirectory": "web/dist",
  "framework": "vite",
  "installCommand": "cd web && npm install"
}
```

### .vercelignore (já configurado ✅)

Ignora:
- `venv/`, `__pycache__/` (Python)
- `data/raw/`, `data/processed/` (dados locais)
- `web/node_modules/` (será instalado no servidor)

---

## 🔧 Configurações Importantes

### Build Settings no Vercel

Se precisar ajustar manualmente no dashboard do Vercel:

**Framework:** Vite  
**Build Command:** `cd web && npm install && npm run build`  
**Output Directory:** `web/dist`  
**Install Command:** `cd web && npm install`  
**Node Version:** 18.x (padrão)

### Variáveis de Ambiente

Não são necessárias para este projeto (dados estáticos).

---

## 🎨 Resultado Esperado

Após o deploy bem-sucedido:

✅ Landing page acessível em: `https://seu-projeto.vercel.app`  
✅ Domínio customizável no dashboard  
✅ SSL/HTTPS automático  
✅ CDN global  
✅ Deploy contínuo (auto-deploy em cada push)

---

## 🐛 Troubleshooting

### Erro: "Command not found: npm"

**Causa:** Node.js não detectado  
**Solução:** Adicione no `vercel.json`:

```json
{
  "build": {
    "env": {
      "NODE_VERSION": "18"
    }
  }
}
```

### Erro: "No such file or directory: web/dist"

**Causa:** Build falhou  
**Solução:** Verifique logs no dashboard do Vercel e confirme que `npm run build` funciona localmente:

```bash
cd web
npm run build
# Deve criar pasta dist/ com arquivos HTML/JS/CSS
```

### Build demora muito (>5 minutos)

**Causa:** Dependências grandes  
**Solução:** Normal na primeira vez. Builds subsequentes usam cache (~30s).

---

## 🚀 Deploy Contínuo

Após o primeiro deploy, o Vercel vai automaticamente:

1. **Detectar novos commits** no GitHub
2. **Rodar build** automaticamente
3. **Fazer deploy** se bem-sucedido
4. **Preview URLs** para branches (não main)

---

## 🎯 Comandos Úteis

```bash
# Ver status do projeto
vercel ls

# Ver detalhes do último deploy
vercel inspect

# Remover projeto do Vercel
vercel remove

# Associar domínio customizado
vercel domains add meu-dominio.com
```

---

## 📊 Checklist de Deploy

- [ ] `vercel.json` configurado corretamente
- [ ] `.vercelignore` atualizado
- [ ] Build local funciona (`cd web && npm run build`)
- [ ] `web/dist/` gerado com sucesso
- [ ] Commit feito no Git
- [ ] Push para GitHub
- [ ] Repositório conectado no Vercel
- [ ] Configurações de build validadas
- [ ] Deploy iniciado
- [ ] Site acessível na URL do Vercel

---

## 🌐 Domínio Customizado

Para usar seu próprio domínio:

1. Acesse **Project Settings → Domains**
2. Adicione seu domínio
3. Configure DNS conforme instruções do Vercel

**Tipos suportados:**
- `meusite.com`
- `www.meusite.com`
- `landing.meusite.com` (subdomínio)

---

**Pronto para deploy?** Faça o commit e push, depois conecte no Vercel! 🚀

**Dúvidas?** Consulte a [documentação oficial do Vercel](https://vercel.com/docs).
