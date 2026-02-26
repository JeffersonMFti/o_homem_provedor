import React from 'react';
import { 
  TrendingDown, Users, MapPin, Code, Database, PieChart, 
  HeartCrack, Info, Github, ExternalLink, MessageCircleHeart, 
  Sparkles, Search, ArrowRight 
} from 'lucide-react';

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

  const allStatesData = [
    { rank: 1, state: 'Distrito Federal', ratio: '4.4', men: '106.755', solteiros: '43.336', mulheres: '192.493' },
    { rank: 2, state: 'Santa Catarina', ratio: '7.8', men: '136.625', solteiros: '41.233', mulheres: '323.591' },
    { rank: 3, state: 'São Paulo', ratio: '8.0', men: '826.134', solteiros: '310.398', mulheres: '2.471.480' },
    { rank: 4, state: 'Mato Grosso', ratio: '8.3', men: '60.153', solteiros: '19.395', mulheres: '160.764' },
    { rank: 5, state: 'Paraná', ratio: '8.6', men: '184.423', solteiros: '59.459', mulheres: '513.123' },
    { rank: 6, state: 'Rio Grande do Sul', ratio: '9.1', men: '163.531', solteiros: '54.085', mulheres: '494.607' },
    { rank: 7, state: 'Mato Grosso do Sul', ratio: '10.4', men: '37.738', solteiros: '12.636', mulheres: '131.445' },
    { rank: 8, state: 'Rio de Janeiro', ratio: '10.5', men: '236.463', solteiros: '92.420', mulheres: '966.718' },
    { rank: 9, state: 'Goiás', ratio: '11.3', men: '94.680', solteiros: '32.568', mulheres: '368.852' },
    { rank: 10, state: 'Espírito Santo', ratio: '11.9', men: '46.416', solteiros: '16.299', mulheres: '193.560' },
    { rank: 11, state: 'Minas Gerais', ratio: '12.5', men: '227.640', solteiros: '91.971', mulheres: '1.149.112' },
    { rank: 12, state: 'Tocantins', ratio: '13.1', men: '15.886', solteiros: '5.472', mulheres: '71.916' },
    { rank: 13, state: 'Rondônia', ratio: '16.2', men: '13.978', solteiros: '4.335', mulheres: '70.053' },
    { rank: 14, state: 'Roraima', ratio: '16.7', men: '5.140', solteiros: '1.794', mulheres: '30.044' },
    { rank: 15, state: 'Amapá', ratio: '18.5', men: '6.316', solteiros: '2.277', mulheres: '42.206' },
    { rank: 16, state: 'Rio Grande do Norte', ratio: '20.7', men: '25.386', solteiros: '8.917', mulheres: '184.712' },
    { rank: 17, state: 'Amazonas', ratio: '21.3', men: '26.691', solteiros: '9.474', mulheres: '201.578' },
    { rank: 18, state: 'Acre', ratio: '22.8', men: '5.447', solteiros: '1.749', mulheres: '39.929' },
    { rank: 19, state: 'Pernambuco', ratio: '23.5', men: '62.541', solteiros: '22.164', mulheres: '520.712' },
    { rank: 20, state: 'Sergipe', ratio: '23.7', men: '16.243', solteiros: '5.712', mulheres: '135.445' },
    { rank: 21, state: 'Paraíba', ratio: '24.0', men: '25.610', solteiros: '8.816', mulheres: '211.596' },
    { rank: 22, state: 'Pará', ratio: '25.5', men: '47.362', solteiros: '15.814', mulheres: '402.714' },
    { rank: 23, state: 'Piauí', ratio: '27.1', men: '17.649', solteiros: '6.652', mulheres: '180.307' },
    { rank: 24, state: 'Ceará', ratio: '27.4', men: '51.478', solteiros: '18.580', mulheres: '508.304' },
    { rank: 25, state: 'Bahia', ratio: '28.2', men: '80.336', solteiros: '30.116', mulheres: '850.450' },
    { rank: 26, state: 'Alagoas', ratio: '29.9', men: '18.015', solteiros: '5.768', mulheres: '172.436' },
    { rank: 27, state: 'Maranhão', ratio: '35.3', men: '29.426', solteiros: '10.266', mulheres: '362.175' }
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
                  Redes sociais têm o poder de transformar <strong>exceção em regra</strong>. Um padrão que existe em bolsões específicos, grandes capitais, setores privilegiados, faixas etárias selecionadas, começa a parecer o mínimo esperável.
                </p>
                <p className="text-stone-600 leading-relaxed mt-4">
                  Este projeto existe para colocar esse número em <strong>perspectiva real</strong>, com dados do mercado formal de trabalho brasileiro.
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
                11.8
              </div>
              <div className="text-2xl md:text-3xl font-bold text-rose-400 mt-4">
                mulheres por homem
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
              <p className="text-lg text-stone-600 max-w-2xl mx-auto">
                Proporção de <strong>mulheres solteiras por cada homem solteiro</strong> que ganha R$ 10k+
              </p>
            </div>
            
            <div className="grid md:grid-cols-2 gap-8">
              {/* Melhores Estados */}
              <div className="backdrop-blur-xl bg-white border border-stone-200 rounded-[2rem] p-8">
                <div className="flex items-center gap-3 mb-6">
                  <div className="px-4 py-2 bg-emerald-100 rounded-xl">
                    <span className="text-xl">🏆</span>
                  </div>
                  <div>
                    <h3 className="text-2xl font-black">Melhores Cenários</h3>
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
                          <div className="text-xs text-stone-600">{item.men} homens 10k+</div>
                        </div>
                      </div>
                      <div className="text-right">
                        <div className="text-2xl font-black text-emerald-600">{item.ratio}</div>
                        <div className="text-xs text-stone-600">mulheres/homem</div>
                      </div>
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
                    <h3 className="text-2xl font-black">Piores Cenários</h3>
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
                          <div className="text-xs text-stone-600">{item.men} homens 10k+</div>
                        </div>
                      </div>
                      <div className="text-right">
                        <div className="text-2xl font-black text-rose-600">{item.ratio}</div>
                        <div className="text-xs text-stone-600">mulheres/homem</div>
                      </div>
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
                  <strong>Como ler:</strong> Em <strong>Distrito Federal</strong>, existem <strong>4.4 mulheres solteiras competindo por cada homem solteiro</strong> que ganha R$ 10k+. 
                  Já no <strong>Maranhão</strong>, são <strong>35.3 mulheres por homem</strong>. 
                  Quanto maior o número, mais acirrada é a competição.
                </div>
              </div>
            </div>
          </div>
        </section>
        
        {/* Dados Completos por Estado */}
        <section className="relative px-6 py-24 bg-white">
          <div className="max-w-7xl mx-auto">
            {/* Header */}
            <div className="text-center mb-16">
              <div className="inline-flex items-center gap-2 px-6 py-3 mb-6 backdrop-blur-xl bg-stone-100 border border-stone-200 rounded-full">
                <Search className="w-4 h-4 text-stone-600" />
                <span className="text-xs uppercase tracking-[0.25em] font-bold text-stone-600">
                  Dados Detalhados
                </span>
              </div>
              
              <h2 className="text-5xl md:text-6xl font-black tracking-tighter leading-[0.9] mb-4">
                Todos os estados
                <span className="block text-gradient">em detalhes</span>
              </h2>
              <p className="text-lg text-stone-600 max-w-2xl mx-auto">
                Ranking completo com dados de todos os 27 estados brasileiros
              </p>
            </div>

            {/* Tabela Responsiva */}
            <div className="backdrop-blur-xl bg-stone-50/80 border border-stone-200 rounded-3xl overflow-hidden">
              {/* Desktop Table */}
              <div className="hidden md:block overflow-x-auto">
                <table className="w-full">
                  <thead className="bg-stone-900 text-white">
                    <tr>
                      <th className="px-6 py-4 text-left text-sm font-black uppercase tracking-wider">#</th>
                      <th className="px-6 py-4 text-left text-sm font-black uppercase tracking-wider">Estado</th>
                      <th className="px-6 py-4 text-center text-sm font-black uppercase tracking-wider">Razão</th>
                      <th className="px-6 py-4 text-right text-sm font-black uppercase tracking-wider">Homens 10k+</th>
                      <th className="px-6 py-4 text-right text-sm font-black uppercase tracking-wider">Solteiros</th>
                      <th className="px-6 py-4 text-right text-sm font-black uppercase tracking-wider">Mulheres Solt.</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-stone-200">
                    {allStatesData.map((item, idx) => (
                      <tr 
                        key={idx} 
                        className={`hover:bg-stone-100 transition-colors ${
                          item.rank <= 3 ? 'bg-emerald-50' : 
                          item.rank >= 25 ? 'bg-rose-50' : 
                          'bg-white'
                        }`}
                      >
                        <td className="px-6 py-4 whitespace-nowrap">
                          <span className={`text-lg font-black ${
                            item.rank <= 3 ? 'text-emerald-600' : 
                            item.rank >= 25 ? 'text-rose-600' : 
                            'text-stone-900'
                          }`}>
                            {item.rank}
                          </span>
                        </td>
                        <td className="px-6 py-4 whitespace-nowrap">
                          <span className="font-bold text-stone-900">{item.state}</span>
                        </td>
                        <td className="px-6 py-4 whitespace-nowrap text-center">
                          <div className="inline-flex flex-col items-center">
                            <span className={`text-xl font-black ${
                              item.rank <= 3 ? 'text-emerald-600' : 
                              item.rank >= 25 ? 'text-rose-600' : 
                              'text-stone-900'
                            }`}>
                              {item.ratio}
                            </span>
                            <span className="text-xs text-stone-500">mulheres/homem</span>
                          </div>
                        </td>
                        <td className="px-6 py-4 whitespace-nowrap text-right font-semibold text-stone-700">
                          {item.men}
                        </td>
                        <td className="px-6 py-4 whitespace-nowrap text-right font-semibold text-blue-600">
                          {item.solteiros}
                        </td>
                        <td className="px-6 py-4 whitespace-nowrap text-right font-semibold text-rose-600">
                          {item.mulheres}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>

              {/* Mobile Cards */}
              <div className="md:hidden p-4 space-y-4">
                {allStatesData.map((item, idx) => (
                  <div 
                    key={idx}
                    className={`p-6 rounded-2xl border-2 ${
                      item.rank <= 3 ? 'bg-emerald-50 border-emerald-200' : 
                      item.rank >= 25 ? 'bg-rose-50 border-rose-200' : 
                      'bg-white border-stone-200'
                    }`}
                  >
                    <div className="flex items-center justify-between mb-4">
                      <div className="flex items-center gap-3">
                        <span className={`text-2xl font-black ${
                          item.rank <= 3 ? 'text-emerald-600' : 
                          item.rank >= 25 ? 'text-rose-600' : 
                          'text-stone-900'
                        }`}>
                          #{item.rank}
                        </span>
                        <span className="text-lg font-bold text-stone-900">{item.state}</span>
                      </div>
                      <div className="text-right">
                        <div className={`text-2xl font-black ${
                          item.rank <= 3 ? 'text-emerald-600' : 
                          item.rank >= 25 ? 'text-rose-600' : 
                          'text-stone-900'
                        }`}>
                          {item.ratio}
                        </div>
                        <div className="text-xs text-stone-500">mulheres/homem</div>
                      </div>
                    </div>
                    
                    <div className="grid grid-cols-3 gap-4 text-center">
                      <div>
                        <div className="text-xs text-stone-500 mb-1">Homens 10k+</div>
                        <div className="font-bold text-stone-700">{item.men}</div>
                      </div>
                      <div>
                        <div className="text-xs text-stone-500 mb-1">Solteiros</div>
                        <div className="font-bold text-blue-600">{item.solteiros}</div>
                      </div>
                      <div>
                        <div className="text-xs text-stone-500 mb-1">Mulheres Solt.</div>
                        <div className="font-bold text-rose-600">{item.mulheres}</div>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Nota Explicativa */}
            <div className="mt-8 p-6 backdrop-blur-xl bg-blue-50/80 border border-blue-200 rounded-2xl">
              <div className="flex gap-3">
                <Info className="w-5 h-5 text-blue-600 flex-shrink-0 mt-0.5" />
                <div className="text-sm text-stone-700 leading-relaxed">
                  <strong>Legenda:</strong> <span className="text-emerald-600 font-bold">Verde</span> indica os 3 melhores cenários. 
                  <span className="text-rose-600 font-bold"> Vermelho</span> indica os 3 piores cenários. 
                  A coluna <strong>Razão</strong> mostra quantas mulheres solteiras existem para cada homem solteiro que ganha R$ 10k+.
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
