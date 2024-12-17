import yt_dlp
from tkinter import Tk, filedialog

def escolher_pasta():
    """Abre uma janela para o usuário selecionar a pasta de salvamento."""
    root = Tk()
    root.withdraw()  # Esconde a janela principal do Tkinter
    root.attributes('-topmost', True)  # Garante que a janela esteja no topo
    caminho = filedialog.askdirectory(title="Escolha a pasta para salvar o vídeo")
    if not caminho:
        print("Nenhuma pasta selecionada. Encerrando o programa.")
        exit()
    return caminho

def baixar_video_com_yt_dlp(youtube_url, caminho_saida):
    """Baixa vídeo do YouTube usando yt-dlp."""
    try:
        print(f"Baixando vídeo: {youtube_url}")
        ydl_opts = {
            'outtmpl': f'{caminho_saida}/%(title)s.%(ext)s',  # Define o nome do arquivo final
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',  # Formato de vídeo e áudio
            'merge_output_format': 'mp4',  # Salva o arquivo final como MP4
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',  # Força a conversão para MP4
            }],
            'postprocessor_args': [
                '-c:v', 'libx264',  # Define o codec de vídeo como H.264
                '-preset', 'fast',  # Ajusta a velocidade de codificação
                '-profile:v', 'high',  # Força o perfil "high", mais compatível com o Premiere
                '-level:v', '4.1',  # Define o nível do H.264 para compatibilidade
                '-c:a', 'aac',  # Define o codec de áudio como AAC
                '-b:a', '192k',  # Define a taxa de bits do áudio
                '-movflags', '+faststart',  # Faz o arquivo ser "streamable", útil para edição
            ],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
        print("Download concluído!")
    except Exception as e:
        print(f"Erro: {e}")

def main():
    while True:
        # Input do link do YouTube
        youtube_url = input("\nCole o link do vídeo do YouTube: ").strip()

        # Escolha da pasta de salvamento
        print("Abrindo janela para escolher local de salvamento...")
        caminho_saida = escolher_pasta()

        # Baixa o vídeo com yt-dlp
        baixar_video_com_yt_dlp(youtube_url, caminho_saida)

        # Pergunta se deseja baixar outro vídeo
        repetir = input("\nDeseja baixar outro vídeo? (s/n): ").strip().lower()
        if repetir != 's':
            print("Encerrando o programa. Obrigado por usar!")
            break

# Executa o programa
if __name__ == "__main__":
    main()
