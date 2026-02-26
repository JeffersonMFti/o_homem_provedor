"""
Servidor HTTP simples para servir a aplicação web do projeto.
Resolve problemas de CORS ao abrir index.html diretamente.

Uso:
    python serve_web.py

Acesse: http://localhost:8000
"""
import http.server
import socketserver
import os
import sys

PORT = 8000
DIRECTORY = "web"

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Adiciona headers CORS para evitar problemas
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

def main():
    # Verifica se o diretório web existe
    if not os.path.exists(DIRECTORY):
        print(f"ERRO: Diretório '{DIRECTORY}' não encontrado.")
        print(f"Execute este script da raiz do projeto.")
        sys.exit(1)

    # Verifica se os arquivos JSON existem
    data_dir = os.path.join(DIRECTORY, 'data')
    required_files = [
        'funil_nacional.json',
        'funil_por_estado.json',
        'distribuicao_renda.json',
        'razao_por_uf.json'
    ]
    
    missing_files = []
    for filename in required_files:
        filepath = os.path.join(data_dir, filename)
        if not os.path.exists(filepath):
            missing_files.append(filename)
    
    if missing_files:
        print("AVISO: Alguns arquivos JSON estão faltando:")
        for f in missing_files:
            print(f"  - {f}")
        print("\nExecute 'python run_pipeline.py' para gerar os dados.")
        print("Continuando mesmo assim...\n")

    # Inicia o servidor
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print("=" * 60)
        print(f"🌐 Servidor rodando em: http://localhost:{PORT}")
        print("=" * 60)
        print(f"\n📂 Servindo arquivos do diretório: {os.path.abspath(DIRECTORY)}")
        print(f"🔗 Abra no navegador: http://localhost:{PORT}/index.html")
        print("\n⌨️  Pressione Ctrl+C para parar o servidor\n")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n🛑 Servidor encerrado.")
            sys.exit(0)

if __name__ == "__main__":
    main()
