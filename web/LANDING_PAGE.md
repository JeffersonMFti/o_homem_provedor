# 🎨 Landing Page React Premium — R$ 10k ou nada?

## 📋 Visão Geral

Landing Page de classe mundial (nível **Awwwards**) criada para apresentar o projeto de Data Storytelling "R$ 10k ou nada?" com design premium inspirado em aplicativos de relacionamento + revista editorial de dados.

## ✨ Características de Design

### 🎯 Design System Implementado

- **Tipografia Extrema**: Textos gigantes com tracking negativo (`text-[12vw]`) contrastando com badges minúsculos (`text-xs tracking-[0.2em]`)
- **Glassmorfismo**: Efeitos de vidro translúcido com `backdrop-blur-xl` e `bg-white/60`
- **Glow Effects**: Sombras coloridas brilhantes usando `blur-3xl` e cores neon
- **Animações Customizadas**: `float` (movimento vertical suave) e `gradient-x` (gradientes animados)
- **Dark Mode Disruptivo**: Seção de revelação com `bg-stone-950` para impacto psicológico
- **Bento Box Layout**: Cards assimétricos com bordas arredondadas extremas (`rounded-[2rem]`)

### 🎨 Paleta de Cores

```javascript
Background: #FDFCFB (off-white)
Textos Neutros: stone-900, stone-500, stone-600
Destaques: rose-500, pink-600, fuchsia-600
Glassmorfismo: white/60, white/80
```

## 🚀 Como Rodar

### Pré-requisitos

- **Node.js** 18+ e npm/yarn

### Instalação e Execução

```bash
# Navegar até a pasta web
cd web

# Instalar dependências
npm install

# Rodar em modo desenvolvimento
npm run dev

# Acessar no navegador
# http://localhost:3000
```

### Build para Produção

```bash
# Gerar build otimizado
npm run build

# Preview do build
npm run preview
```

## 📦 Stack Tecnológica

### Core
- **React 18.2** — Componentes funcionais modernos
- **Vite 5.1** — Build tool ultra-rápido
- **Tailwind CSS 3.4** — Utility-first CSS framework

### UI/UX
- **lucide-react** — Ícones SVG de alta qualidade (14 ícones importados)
- **Inter Font** — Tipografia premium via Google Fonts

### Ferramentas de Build
- **PostCSS** + **Autoprefixer** — Processamento CSS
- **@vitejs/plugin-react** — Fast Refresh e JSX

## 🎭 Componentes e Seções

### 1. **Hero Section**
- Título gigante com tracking negativo
- Badge superior com glassmorfismo
- Gradiente animado no texto "ou nada?"
- CTAs com glow effects
- Ícone flutuante (animate-float)

### 2. **Contexto**
- Grid 2 colunas responsivo
- Card glassmórfico com estatísticas
- Barra de progresso animada (5.17%)

### 3. **O Funil (Bento Box)**
- 3 cards assimétricos
- Mini charts inline
- Ícones coloridos em badges
- Hover states com transições suaves

### 4. **A Grande Revelação** ⭐
- **Seção Dark Mode Disruptiva**
- Número gigante `11.8x` com gradiente animado
- Glow effects intensos (`glow-rose-strong`)
- Background `bg-stone-950` para contraste

### 5. **Geografia da Escassez**
- Grid 2 colunas (Melhores × Piores estados)
- Cards com cores semânticas (emerald = bom, rose = ruim)
- Rankings numerados
- Nota explicativa com ícone de info

### 6. **Stack Técnica**
- Grid 3 colunas responsivo
- Cards com hover effects
- Nota de transparência destacada

### 7. **CTA Final**
- Background gradient complexo
- Título gigante animado
- Botões de ação principais
- Footer com créditos

## 🎨 Animações Customizadas

```css
@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-20px); }
}

@keyframes gradient-x {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}
```

**Aplicação:**
- `.animate-float` — Movimento vertical suave (6s)
- `.animate-gradient` — Gradiente horizontal animado (3s)
- `.text-gradient` — Texto com gradiente rose/pink/fuchsia

## 📊 Dados Incorporados

Os dados estão embutidos diretamente no componente (sem necessidade de API):

```javascript
const incomeData = [...]; // Distribuição de renda
const topStates = [...];  // 3 melhores estados
const bottomStates = [...]; // 3 piores estados
```

**Fonte:** IBGE Censo Demográfico 2022

## 🎯 Responsividade

- **Mobile First**: Design otimizado para mobile
- **Breakpoints Tailwind**: `sm:`, `md:`, `lg:`
- **Tipografia Fluida**: Usa `vw` units para escalar textos automaticamente
- **Grid Adaptativo**: Layouts que colapsam graciosamente em mobile

## 🔧 Customização

### Alterar Cores

Edite [tailwind.config.js](tailwind.config.js):

```javascript
theme: {
  extend: {
    colors: {
      // Adicione suas cores personalizadas
    },
  },
}
```

### Adicionar Seções

Edite [LandingPage.jsx](LandingPage.jsx) e adicione novos `<section>` com as mesmas convenções de design.

### Modificar Dados

Altere os arrays no topo do componente:
- `incomeData`
- `topStates`
- `bottomStates`

## 📁 Estrutura de Arquivos

```
web/
├── LandingPage.jsx         # Componente principal (único arquivo necessário!)
├── main.jsx                # Entry point React
├── index-react.html        # HTML base com fonts
├── index.css               # Tailwind directives
├── package.json            # Dependências
├── vite.config.js          # Configuração Vite
├── tailwind.config.js      # Configuração Tailwind
├── postcss.config.js       # PostCSS setup
└── LANDING_PAGE.md         # Esta documentação
```

## 🎓 Conceitos Avançados Implementados

### 1. **Glassmorfismo Profissional**
```jsx
className="backdrop-blur-xl bg-white/60 border border-white/50"
```

### 2. **Glow Effects Customizados**
```jsx
className="glow-rose-strong"
// box-shadow: 0 0 120px rgba(236, 72, 153, 0.5)
```

### 3. **Tipografia com Tracking Negativo**
```jsx
className="text-[12vw] tracking-tighter leading-[0.85]"
```

### 4. **Gradientes Animados**
```jsx
className="text-gradient animate-gradient"
// Usa @keyframes gradient-x
```

### 5. **Dark Mode Disruptivo**
```jsx
<section className="bg-stone-950"> {/* Quebra o padrão visual */}
```

### 6. **Bento Box Layout**
```jsx
<div className="grid md:grid-cols-3 gap-6">
  {/* Cards com rounded-[2rem] */}
</div>
```

## 🚨 Notas Importantes

1. **Não deletar `index.html` e `main.js`** — São os arquivos originais do projeto. Esta landing page é uma **adição**, não substitui a visualização de dados existente.

2. **Porta diferente** — A landing page roda na porta `3000`, enquanto o servidor Python usa `8000`.

3. **Fontes externas** — Usa Google Fonts (Inter). Certifique-se de ter conexão com internet na primeira execução.

4. **Performance** — O Vite faz code splitting e tree shaking automático para builds otimizados.

## 🎬 Next Steps

- [ ] Adicionar smooth scroll entre seções
- [ ] Implementar lazy loading de imagens (se adicionar fotos)
- [ ] Adicionar meta tags OpenGraph para compartilhamento social
- [ ] Criar variantes de cores (tema dark completo)
- [ ] Adicionar micro-interações com Framer Motion
- [ ] Implementar loading states
- [ ] Adicionar testes com Vitest

## 📝 Créditos

**Design & Development**: Landing Page de classe mundial  
**Inspiração**: Awwwards, Dribbble, app de relacionamento premium  
**Dados**: IBGE Censo Demográfico 2022  
**Tipografia**: Inter (Google Fonts)  
**Ícones**: Lucide React

---

**Desenvolvido com 💖 usando React, Tailwind CSS e muito bom gosto.**
