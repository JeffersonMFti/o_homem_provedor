import React, { useEffect } from 'react';
import { 
  TrendingDown, Users, MapPin, Code, Database, PieChart, 
  HeartCrack, Info, Github, ExternalLink, MessageCircleHeart, 
  Sparkles, Search, ArrowRight 
} from 'lucide-react';
import Lenis from '@studio-freight/lenis';
import { ZoomParallax } from './src/components/ui/ZoomParallax';

// Animações customizadas
const styles = `
  @keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-20px); }
  }
  
  @keyframes gradient-x {
    0%, 100% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
  }
  
  .animate-float {
    animation: float 6s ease-in-out infinite;
  }
  
  .animate-gradient {
    background-size: 200% 200%;
    animation: gradient-x 3s ease infinite;
  }
  
  .text-gradient {
    background: linear-gradient(135deg, #be123c, #ec4899, #f472b6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }
  
  .glow-rose {
    box-shadow: 0 0 80px rgba(244, 114, 182, 0.3);
  }
  
  .glow-rose-strong {
    box-shadow: 0 0 120px rgba(236, 72, 153, 0.5), 0 0 60px rgba(244, 114, 182, 0.3);
  }
`;

const LandingPage = () => {
  // Smooth scroll configuration
  useEffect(() => {
    const lenis = new Lenis({
      duration: 1.2,
      easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
      smoothWheel: true,
    });
   
    function raf(time) {
      lenis.raf(time);
      requestAnimationFrame(raf);
    }

    requestAnimationFrame(raf);

    return () => {
      lenis.destroy();
    };
  }, []);

  // Dados do projeto
  const incomeData = [
    { label: 'Até 2 SM', percent: 64.6, color: 'bg-stone-200' },
    { label: '2 a 5 SM', percent: 26.6, color: 'bg-stone-300' }, 
    { label: '5 a 10 SM', percent: 5.7, color: 'bg-stone-400' },
    { label: '10k+ (O Alvo)', percent: 3.2, color: 'bg-rose-500', highlight: true } 
  ];
  
  const topStates = [
    { state: 'Distrito Federal', ratio: '4.4x', men: '106.755' },
    { state: 'Santa Catarina', ratio: '7.8x', men: '136.625' },
    { state: 'São Paulo', ratio: '8.0x', men: '826.134' }
  ];
  
  const bottomStates = [
    { state: 'Bahia', ratio: '28.2x', men: '80.336' },
    { state: 'Alagoas', ratio: '29.9x', men: '18.015' },
    { state: 'Maranhão', ratio: '35.3x', men: '29.426' }
  ];

  // Imagens para o Zoom Parallax Effect
  const parallaxImages = [
    {
      src: 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1280&h=720&fit=crop&q=80',
      alt: 'Gráficos e análise de dados',
    },
    {
      src: 'https://images.unsplash.com/photo-1529156069898-49953e39b3ac?w=1280&h=720&fit=crop&q=80',
      alt: 'Casal feliz - relacionamentos',
    },
    {
      src: 'https://images.unsplash.com/photo-1523287562758-66c7fc58967f?w=800&h=800&fit=crop&q=80',
      alt: 'Pessoas trabalhando - mercado de trabalho',
    },
    {
      src: 'https://images.unsplash.com/photo-1483389127117-b6a2102724ae?w=1280&h=720&fit=crop&q=80',
      alt: 'Cidade de São Paulo - Brasil',
    },
    {
      src: 'https://images.unsplash.com/photo-1522071820081-009f0129c71c?w=800&h=800&fit=crop&q=80',
      alt: 'Equipe diversa - população brasileira',
    },
    {
      src: 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1280&h=720&fit=crop&q=80',
      alt: 'Dashboard com estatísticas',
    },
    {
      src: 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=1280&h=720&fit=crop&q=80',
      alt: 'Match de relacionamento - dating app',
    },
  ];

  return (
    <>
      <style>{styles}</style>
      
      <div className="min-h-screen bg-[#FDFCFB] text-stone-900 overflow-x-hidden">
        
        {/* Hero Section - Tipografia Extrema */}
        <section className="relative min-h-screen flex items-center justify-center px-6 py-20 overflow-hidden">
          {/* Background Glow Effects */}
          <div className="absolute top-0 right-0 w-[500px] h-[500px] bg-rose-300/20 rounded-full blur-3xl"></div>
          <div className="absolute bottom-0 left-0 w-[600px] h-[600px] bg-pink-300/20 rounded-full blur-3xl"></div>
          
          <div className="relative z-10 max-w-7xl mx-auto text-center">
            {/* Badge Superior */}
            <div className="inline-flex items-center gap-2 px-6 py-2 mb-8 backdrop-blur-xl bg-white/60 border border-rose-200/50 rounded-full">
              <Sparkles className="w-4 h-4 text-rose-500" />
              <span className="text-xs uppercase tracking-[0.2em] font-bold text-stone-600">
                Data Storytelling · Censo IBGE 2022
              </span>
            </div>
            
            {/* Título Gigante com Tracking Negativo */}
            <h1 className="text-[12vw] md:text-[10vw] lg:text-[8vw] font-black tracking-tighter leading-[0.85] mb-6">
              R$ 10k
              <span className="block text-gradient animate-gradient">ou nada?</span>
            </h1>
            
            {/* Subtítulo */}
            <p className="text-xl md:text-2xl text-stone-600 max-w-3xl mx-auto mb-12 leading-relaxed">
              A frase que viralizou. A matemática que ninguém foi atrás.
              <span className="block mt-2 text-stone-500">
                Uma análise brutal sobre expectativas × realidade no mercado de relacionamentos brasileiro.
              </span>
            </p>
            
            {/* CTA Buttons */}
            <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
              <button className="group px-8 py-4 bg-gradient-to-r from-rose-500 to-pink-600 text-white rounded-2xl font-bold text-lg shadow-lg hover:shadow-xl transition-all duration-300 glow-rose flex items-center gap-2">
                <Search className="w-5 h-5" />
                Explore os Dados
                <ArrowRight className="w-5 h-5 group-hover:translate-x-1 transition-transform" />
              </button>
              
              <a 
                href="https://github.com/JeffersonMFti/o_homem_provedor" 
                target="_blank" 
                rel="noopener noreferrer"
                className="px-8 py-4 backdrop-blur-xl bg-white/60 border-2 border-stone-200 rounded-2xl font-bold text-lg hover:border-rose-300 transition-all duration-300 flex items-center gap-2"
              >
                <Github className="w-5 h-5" />
                Ver no GitHub
              </a>
            </div>
            
            {/* Floating Icon */}
            <div className="mt-16 animate-float">
              <MessageCircleHeart className="w-16 h-16 mx-auto text-rose-400 opacity-40" />
            </div>
          </div>
        </section>
        
        {/* Contexto - Glassmorfismo */}
        <section className="relative px-6 py-24">
          <div className="max-w-6xl mx-auto">
            {/* Badge da Seção */}
            <div className="inline-flex items-center gap-2 px-4 py-2 mb-6 backdrop-blur-xl bg-white/60 border border-stone-200/50 rounded-full">
              <Info className="w-3.5 h-3.5 text-stone-600" />
              <span className="text-xs uppercase tracking-[0.2em] font-bold text-stone-600">Contexto</span>
            </div>
            
            <div className="grid md:grid-cols-2 gap-8 items-center">
              {/* Texto */}
              <div>
                <h2 className="text-5xl md:text-6xl font-black tracking-tighter leading-[0.9] mb-6">
                  A frase que
                  <span className="block">tomou as redes.</span>
                </h2>
                <p className="text-lg text-stone-600 leading-relaxed mb-4">
                  <em>"Pra namorar comigo, ele precisa ganhar pelo menos 10 mil por mês."</em>
                </p>
                <p className="text-stone-600 leading-relaxed">
                  Redes sociais têm o poder de transformar <strong>exceção em regra</strong>. 
                  Um padrão que existe em bolsões específicos — grandes capitais, setores privilegiados, 
                  faixas etárias selecionadas — começa a parecer o mínimo esperável.
                </p>
                <p className="text-stone-600 leading-relaxed mt-4">
                  Este projeto existe para colocar esse número em <strong>perspectiva real</strong>, 
                  com dados do mercado formal de trabalho brasileiro.
                </p>
              </div>
              
              {/* Card Glassmórfico */}
              <div className="relative">
                <div className="absolute inset-0 bg-gradient-to-br from-rose-300/30 to-pink-300/30 rounded-[2rem] blur-2xl"></div>
                <div className="relative backdrop-blur-xl bg-white/60 border border-white/50 rounded-[2rem] p-8 shadow-xl">
                  <div className="flex items-center gap-4 mb-6">
                    <div className="p-4 bg-gradient-to-br from-rose-500 to-pink-600 rounded-2xl">
                      <Users className="w-8 h-8 text-white" />
                    </div>
                    <div>
                      <div className="text-4xl font-black tracking-tight">49.7M</div>
                      <div className="text-sm text-stone-600">Homens ocupados no Brasil</div>
                    </div>
                  </div>
                  
                  <div className="space-y-3">
                    <div className="flex justify-between items-center">
                      <span className="text-stone-600">Que ganham 10k+</span>
                      <span className="text-2xl font-black text-rose-600">5.17%</span>
                    </div>
                    <div className="h-3 bg-stone-200 rounded-full overflow-hidden">
                      <div className="h-full bg-gradient-to-r from-rose-500 to-pink-600" style={{ width: '5.17%' }}></div>
                    </div>
                    <div className="text-xs text-stone-500 pt-2">
                      Apenas 2.57 milhões em todo o país
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
        
        {/* O Funil - Bento Box Layout */}
        <section className="relative px-6 py-24 bg-gradient-to-b from-transparent to-stone-50">
          <div className="max-w-7xl mx-auto">
            {/* Header da Seção */}
            <div className="text-center mb-16">
              <div className="inline-flex items-center gap-2 px-4 py-2 mb-6 backdrop-blur-xl bg-white/60 border border-stone-200/50 rounded-full">
                <TrendingDown className="w-3.5 h-3.5 text-rose-600" />
                <span className="text-xs uppercase tracking-[0.2em] font-bold text-stone-600">O Filtro Implacável</span>
              </div>
              
              <h2 className="text-6xl md:text-7xl font-black tracking-tighter leading-[0.85] mb-4">
                Do Brasil inteiro
                <span className="block text-gradient">até o match</span>
              </h2>
              <p className="text-lg text-stone-600 max-w-2xl mx-auto">
                Uma jornada em três etapas que transforma 49 milhões em... bem, você vai ver.
              </p>
            </div>
            
            {/* Bento Grid */}
            <div className="grid md:grid-cols-3 gap-6">
              {/* Card 1 - Renda */}
              <div className="group relative backdrop-blur-xl bg-white/80 border border-stone-200/50 rounded-[2rem] p-8 hover:bg-white transition-all duration-300 hover:shadow-2xl">
                <div className="absolute top-8 right-8 p-3 bg-rose-100 rounded-2xl">
                  <PieChart className="w-6 h-6 text-rose-600" />
                </div>
                
                <div className="mb-6">
                  <div className="text-5xl font-black mb-2">01</div>
                  <h3 className="text-3xl font-black tracking-tight">A Renda</h3>
                </div>
                
                <p className="text-stone-600 mb-6 leading-relaxed">
                  Qual o percentual de homens que <strong>de fato</strong> recebe R$ 10.000 ou mais por mês?
                </p>
                
                {/* Mini Chart */}
                <div className="space-y-2">
                  {incomeData.map((item, idx) => (
                    <div key={idx} className="flex items-center gap-3">
                      <div className="flex-1">
                        <div className="flex justify-between text-xs mb-1">
                          <span className={item.highlight ? 'font-bold text-rose-600' : 'text-stone-600'}>
                            {item.label}
                          </span>
                          <span className={item.highlight ? 'font-black text-rose-600' : 'font-bold text-stone-900'}>
                            {item.percent}%
                          </span>
                        </div>
                        <div className="h-2 bg-stone-100 rounded-full overflow-hidden">
                          <div 
                            className={`${item.color} h-full transition-all duration-1000`}
                            style={{ width: `${item.percent}%` }}
                          ></div>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
              
              {/* Card 2 - Disponibilidade */}
              <div className="group relative backdrop-blur-xl bg-white/80 border border-stone-200/50 rounded-[2rem] p-8 hover:bg-white transition-all duration-300 hover:shadow-2xl">
                <div className="absolute top-8 right-8 p-3 bg-pink-100 rounded-2xl">
                  <HeartCrack className="w-6 h-6 text-pink-600" />
                </div>
                
                <div className="mb-6">
                  <div className="text-5xl font-black mb-2">02</div>
                  <h3 className="text-3xl font-black tracking-tight">O Estado Civil</h3>
                </div>
                
                <p className="text-stone-600 mb-8 leading-relaxed">
                  Desse grupo, quantos estão <strong>solteiros</strong>? O pool afunila consideravelmente.
                </p>
                
                {/* Estatística Grande */}
                <div className="relative">
                  <div className="absolute inset-0 bg-gradient-to-br from-pink-200/50 to-rose-200/50 rounded-3xl blur-xl"></div>
                  <div className="relative bg-gradient-to-br from-pink-50 to-rose-50 rounded-3xl p-6 text-center border border-pink-200">
                    <div className="text-6xl font-black text-gradient mb-2">56.3%</div>
                    <div className="text-sm text-stone-600 font-medium">são solteiros ou desquitados</div>
                    <div className="mt-4 text-xs text-stone-500">
                      Pool final: <strong className="text-stone-900">~1.45 milhões</strong>
                    </div>
                  </div>
                </div>
              </div>
              
              {/* Card 3 - A Proporção */}
              <div className="group relative backdrop-blur-xl bg-white/80 border border-stone-200/50 rounded-[2rem] p-8 hover:bg-white transition-all duration-300 hover:shadow-2xl">
                <div className="absolute top-8 right-8 p-3 bg-fuchsia-100 rounded-2xl">
                  <Users className="w-6 h-6 text-fuchsia-600" />
                </div>
                
                <div className="mb-6">
                  <div className="text-5xl font-black mb-2">03</div>
                  <h3 className="text-3xl font-black tracking-tight">A Proporção</h3>
                </div>
                
                <p className="text-stone-600 mb-8 leading-relaxed">
                  Quantas mulheres solteiras existem? A <strong>oferta × demanda</strong> final.
                </p>
                
                {/* Comparação Visual */}
                <div className="space-y-4">
                  <div>
                    <div className="flex items-center justify-between mb-2">
                      <span className="text-sm text-stone-600">Homens 10k+ solteiros</span>
                      <span className="font-black text-stone-900">1.45M</span>
                    </div>
                    <div className="h-12 bg-stone-900 rounded-xl flex items-center justify-center">
                      <Users className="w-6 h-6 text-white" />
                    </div>
                  </div>
                  
                  <div className="text-center text-2xl font-black text-stone-400">VS</div>
                  
                  <div>
                    <div className="flex items-center justify-between mb-2">
                      <span className="text-sm text-stone-600">Mulheres solteiras (25-49 anos)</span>
                      <span className="font-black text-rose-600">17.1M</span>
                    </div>
                    <div className="h-24 bg-gradient-to-r from-rose-500 to-pink-500 rounded-xl flex items-center justify-center">
                      <div className="flex gap-1">
                        {[...Array(8)].map((_, i) => (
                          <Users key={i} className="w-4 h-4 text-white" />
                        ))}
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
        
        {/* Zoom Parallax Transition */}
        <ZoomParallax images={parallaxImages} />
        
        {/* A GRANDE REVELAÇÃO - Dark Mode Disruptivo */}
        <section className="relative px-6 py-32 bg-stone-950 overflow-hidden">
          {/* Glow Effects Intensos */}
          <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] bg-rose-500/20 rounded-full blur-3xl glow-rose-strong"></div>
          
          <div className="relative z-10 max-w-5xl mx-auto text-center">
            {/* Badge */}
            <div className="inline-flex items-center gap-2 px-6 py-3 mb-12 backdrop-blur-xl bg-rose-950/40 border border-rose-500/30 rounded-full">
              <HeartCrack className="w-4 h-4 text-rose-400" />
              <span className="text-xs uppercase tracking-[0.25em] font-bold text-rose-400">
                A Matemática Final
              </span>
            </div>
            
            {/* Número Gigante */}
            <div className="mb-8">
              <div className="text-[20vw] md:text-[15vw] font-black tracking-tighter leading-[0.8] text-transparent bg-clip-text bg-gradient-to-r from-rose-500 via-pink-500 to-rose-400 animate-gradient">
                11.8x
              </div>
            </div>
            
            {/* Explicação */}
            <h2 className="text-4xl md:text-5xl font-black text-white mb-6 tracking-tight">
              Para cada homem solteiro que ganha R$ 10k+
            </h2>
            <p className="text-2xl md:text-3xl text-rose-400 font-bold mb-8">
              existem quase <span className="text-rose-300">12 mulheres</span> solteiras competindo
            </p>
            
            <div className="max-w-2xl mx-auto">
              <p className="text-lg text-stone-400 leading-relaxed mb-6">
                É a proporção nacional. Mas calma: esse número <strong className="text-white">varia absurdamente</strong> por estado. 
                Em alguns lugares é mais tranquilo. Em outros... bem, é Jogos Vorazes.
              </p>
              
              {/* Botão de Destaque */}
              <a 
                href="#geografia" 
                className="group mx-auto px-10 py-5 bg-gradient-to-r from-rose-600 to-pink-600 text-white rounded-2xl font-black text-xl shadow-2xl hover:shadow-rose-500/50 transition-all duration-300 glow-rose-strong flex items-center gap-3"
              >
                Ver por Estado
                <MapPin className="w-6 h-6 group-hover:scale-110 transition-transform" />
              </a>
            </div>
          </div>
        </section>
        
        {/* Geografia da Escassez */}
        <section id="geografia" className="relative px-6 py-24 bg-stone-50">
          <div className="max-w-6xl mx-auto">
            {/* Header */}
            <div className="text-center mb-16">
              <div className="inline-flex items-center gap-2 px-4 py-2 mb-6 backdrop-blur-xl bg-white/60 border border-stone-200/50 rounded-full">
                <MapPin className="w-3.5 h-3.5 text-stone-600" />
                <span className="text-xs uppercase tracking-[0.2em] font-bold text-stone-600">Geografia da Escassez</span>
              </div>
              
              <h2 className="text-5xl md:text-6xl font-black tracking-tighter leading-[0.9] mb-4">
                Os melhores e
                <span className="block text-gradient">os piores estados</span>
              </h2>
            </div>
            
            <div className="grid md:grid-cols-2 gap-8">
              {/* Melhores Estados */}
              <div className="backdrop-blur-xl bg-white border border-stone-200 rounded-[2rem] p-8">
                <div className="flex items-center gap-3 mb-6">
                  <div className="px-4 py-2 bg-emerald-100 rounded-xl">
                    <span className="text-xl">🏆</span>
                  </div>
                  <div>
                    <h3 className="text-2xl font-black">Melhores Odds</h3>
                    <p className="text-sm text-stone-600">Onde a competição é menos acirrada</p>
                  </div>
                </div>
                
                <div className="space-y-4">
                  {topStates.map((item, idx) => (
                    <div key={idx} className="flex items-center justify-between p-4 bg-emerald-50 border border-emerald-200 rounded-2xl">
                      <div className="flex items-center gap-3">
                        <div className="text-2xl font-black text-emerald-600">#{idx + 1}</div>
                        <div>
                          <div className="font-bold text-stone-900">{item.state}</div>
                          <div className="text-xs text-stone-600">{item.men} homens</div>
                        </div>
                      </div>
                      <div className="text-2xl font-black text-emerald-600">{item.ratio}</div>
                    </div>
                  ))}
                </div>
              </div>
              
              {/* Piores Estados */}
              <div className="backdrop-blur-xl bg-white border border-stone-200 rounded-[2rem] p-8">
                <div className="flex items-center gap-3 mb-6">
                  <div className="px-4 py-2 bg-rose-100 rounded-xl">
                    <span className="text-xl">💔</span>
                  </div>
                  <div>
                    <h3 className="text-2xl font-black">Piores Odds</h3>
                    <p className="text-sm text-stone-600">Onde a fila é mais longa</p>
                  </div>
                </div>
                
                <div className="space-y-4">
                  {bottomStates.map((item, idx) => (
                    <div key={idx} className="flex items-center justify-between p-4 bg-rose-50 border border-rose-200 rounded-2xl">
                      <div className="flex items-center gap-3">
                        <div className="text-2xl font-black text-rose-600">#{27 - idx}</div>
                        <div>
                          <div className="font-bold text-stone-900">{item.state}</div>
                          <div className="text-xs text-stone-600">{item.men} homens</div>
                        </div>
                      </div>
                      <div className="text-2xl font-black text-rose-600">{item.ratio}</div>
                    </div>
                  ))}
                </div>
              </div>
            </div>
            
            {/* Nota */}
            <div className="mt-8 p-6 backdrop-blur-xl bg-amber-50/80 border border-amber-200 rounded-2xl">
              <div className="flex gap-3">
                <Info className="w-5 h-5 text-amber-600 flex-shrink-0 mt-0.5" />
                <div className="text-sm text-stone-700 leading-relaxed">
                  <strong>Nota:</strong> A proporção varia de <strong>4.4x</strong> (DF) até <strong>35.3x</strong> (MA). 
                  Fatores como industrialização, PIB per capita e concentração de empregos formais explicam essa disparidade.
                </div>
              </div>
            </div>
          </div>
        </section>
        
        {/* Stack Técnica */}
        <section className="relative px-6 py-24 bg-gradient-to-b from-stone-50 to-white">
          <div className="max-w-5xl mx-auto">
            <div className="text-center mb-16">
              <div className="inline-flex items-center gap-2 px-4 py-2 mb-6 backdrop-blur-xl bg-white/60 border border-stone-200/50 rounded-full">
                <Code className="w-3.5 h-3.5 text-stone-600" />
                <span className="text-xs uppercase tracking-[0.2em] font-bold text-stone-600">Stack Técnica</span>
              </div>
              
              <h2 className="text-5xl md:text-6xl font-black tracking-tighter leading-[0.9]">
                Feito com dados
                <span className="block text-gradient">oficiais do IBGE</span>
              </h2>
            </div>
            
            <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
              {[
                { icon: Database, title: 'Censo 2022', desc: 'IBGE via API SIDRA' },
                { icon: Code, title: 'Python', desc: 'Pandas, NumPy, Plotly' },
                { icon: PieChart, title: 'Visualização', desc: 'Gráficos interativos' },
              ].map((item, idx) => (
                <div key={idx} className="group p-6 backdrop-blur-xl bg-white/80 border border-stone-200 rounded-2xl hover:border-rose-300 transition-all duration-300 hover:shadow-xl">
                  <div className="p-3 bg-stone-100 rounded-xl w-fit mb-4 group-hover:bg-rose-50 transition-colors">
                    <item.icon className="w-6 h-6 text-stone-700 group-hover:text-rose-600 transition-colors" />
                  </div>
                  <h3 className="font-black text-xl mb-2">{item.title}</h3>
                  <p className="text-stone-600 text-sm">{item.desc}</p>
                </div>
              ))}
            </div>
            
            {/* Nota de Transparência */}
            <div className="mt-12 p-8 backdrop-blur-xl bg-stone-100/80 border border-stone-200 rounded-[2rem]">
              <h3 className="font-black text-2xl mb-4 flex items-center gap-2">
                <span className="text-2xl">🔍</span>
                Transparência Total
              </h3>
              <p className="text-stone-700 leading-relaxed mb-4">
                Todos os dados utilizados são <strong>públicos e verificáveis</strong>. 
                Nenhum número foi estimado ou fabricado. O que está aqui é o que o Brasil reportou sobre si mesmo 
                no Censo Demográfico de 2022 (tabelas SIDRA 10292, 10185 e 10268).
              </p>
              <p className="text-stone-600 text-sm">
                O código-fonte completo está disponível no GitHub para auditoria.
              </p>
            </div>
          </div>
        </section>
        
        {/* CTA Final */}
        <section className="relative px-6 py-32 overflow-hidden">
          {/* Background Gradient */}
          <div className="absolute inset-0 bg-gradient-to-br from-rose-100 via-pink-50 to-fuchsia-100"></div>
          <div className="absolute top-0 right-0 w-[600px] h-[600px] bg-rose-300/30 rounded-full blur-3xl"></div>
          <div className="absolute bottom-0 left-0 w-[500px] h-[500px] bg-pink-300/30 rounded-full blur-3xl"></div>
          
          <div className="relative z-10 max-w-4xl mx-auto text-center">
            <h2 className="text-6xl md:text-7xl font-black tracking-tighter leading-[0.85] mb-6">
              Dados não julgam.
              <span className="block text-gradient animate-gradient">Apenas informam.</span>
            </h2>
            
            <p className="text-xl text-stone-600 max-w-2xl mx-auto mb-12 leading-relaxed">
              Este projeto não invalida expectativas pessoais. Apenas coloca números em perspectiva. 
              Quando você entende o tamanho real de um grupo, fica mais fácil separar exceção de regra.
            </p>
            
            <div className="flex flex-col sm:flex-row gap-6 justify-center">
              <a 
                href="https://github.com/JeffersonMFti/o_homem_provedor" 
                target="_blank" 
                rel="noopener noreferrer"
                className="group px-10 py-5 bg-stone-900 text-white rounded-2xl font-bold text-lg shadow-xl hover:shadow-2xl transition-all duration-300 flex items-center gap-3 justify-center"
              >
                <Github className="w-6 h-6" />
                Ver Repositório Completo
                <ExternalLink className="w-5 h-5 group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform" />
              </a>
              
              <button className="px-10 py-5 backdrop-blur-xl bg-white/80 border-2 border-stone-300 text-stone-900 rounded-2xl font-bold text-lg hover:border-rose-400 transition-all duration-300 flex items-center gap-3 justify-center">
                <Database className="w-6 h-6" />
                Explorar Dashboard
              </button>
            </div>
            
            {/* Footer Credits */}
            <div className="mt-16 pt-8 border-t border-stone-300">
              <p className="text-sm text-stone-600">
                Desenvolvido com Python, React e Tailwind CSS •{' '}
                <a 
                  href="https://github.com/JeffersonMFti" 
                  target="_blank" 
                  rel="noopener noreferrer"
                  className="font-bold hover:text-rose-600 transition-colors"
                >
                  Jefferson Monteiro
                </a>
              </p>
              <p className="text-xs text-stone-500 mt-2">
                Fonte: IBGE — Censo Demográfico 2022
              </p>
            </div>
          </div>
        </section>
        
      </div>
    </>
  );
};

export default LandingPage;
