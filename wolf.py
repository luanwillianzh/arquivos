#!/usr/bin/env python3
import os
import sys
import subprocess
from time import sleep

# Configurações
PASTA_DOWNLOADS = "/sdcard/wolfvideos"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
ARQUIVO_COOKIES = "/sdcard/cookies.txt"

# Criar pasta de downloads se não existir
os.makedirs(PASTA_DOWNLOADS, exist_ok=True)

# Banner WOLF VIDEOS estilizado
def mostrar_banner():
    print("""\033[1;33m
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠀⠀⢀⣀⡀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠔⠊⠉⠀⠀⠀⠀⢀⡤⠛⠋⠁⠀⠈⠉⠓⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠊⠀⠀⠀⠀⠀⠀⠀⣰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠐⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣰⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⡇⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠁⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡀⡆⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣾⣟⠛⠋⠩⠿⣶⣤⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⣻⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣟⣠⠀⢤⠔⢍⣿⣿⣷⣄
⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⡇⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡿⣿⡟⣫⣸⣿⣅⣄⣴⣾⠿⠛⠋⠹⣧
⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⢹⠀⠀⠀⠀⠀⠀⠀⣠⡿⠃⠈⠀⣼⠿⠛⠉⠉⠁⠀⠀⠀⣠⠔⠀⠹⣇
⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⢸⠓⠦⠄⣀⣀⣀⡴⠿⠿⣤⣴⡴⠁⠀⠀⣲⣄⡤⠔⠚⡏⣼⡇⠀⢠⣸
⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡯⠀⠘⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠉⢣⡀⣠⠞⢻⣿⣿⠦⣼⣟⣁⡇⢠⠀⢻
⠀⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠃⠀⠀⠀⠀⠼⣏⢿⣷⡗⢸⢀⣿
⠀⠀⠀⠀⠀⠀⠀⠐⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀⠀⠀⠀⠀⠀⠸⣶⠃⠀⠀⠀⠀⠀⢘⡇⠀⢀⡀⠀⠠⠞⣰⣿⠃⣼⠟
⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠃⠀⠀⠀⠀⠀⠀⠀⠀⡍⠀⠀⠀⠀⠀⠀⣼⢇⠀⠀⠯⣯⣵⣾⣿⣿⡾⠋⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠀⠀⠀⠀⠀⠀⠀⠀⣼⠁⠀⠀⠀⠀⠀⣰⠻⠊⠓⠒⣿⣿⣿⣿⡿⡟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠗⠀⠀⠀⠀⠀⠀⠀⢠⠃⠀⠀⠀⠀⠀⢠⠃⠀⠀⠀⠀⠹⡿⣿⢹⣾⠇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀⠀⠀⠀⠀⠀⠀⢀⡏⠀⠀⠀⠀⠀⢠⠋⠀⠀⠀⠀⠀⠀⠀⠈⠀⠛⠀⠀
⠀⠀⠀⠀⠀⢀⣀⣠⣇⣀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀⠀⠀⠈⡇⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⢀⣰⣻⠀⠀⠀⠀⠀⢀⠎⣀⣲⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣀⠴⠚⠉⠀⢀⣀⣨⣉⡒⠢⣄⠀⠀⠀⢀⡇⠀⣠⠔⠚⠉⠉⠈⠙⠲⢤⡆⠀⠀⠀⢸⣅⠀⠀⠀⠀⣠⠞⢡⠇⠀⠀⠀⠀⠀⣞⠛⢿⠉⠁⠀⠈⠓⠦⡀⠀⠀⠀⠀⠀⠀
⠒⠈⠀⠀⠀⠀⢰⠃⢄⠀⠀⠉⠒⠮⣄⣀⣠⠼⠖⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⣄⠀⠀⣾⡈⠑⠲⠴⠊⠁⠀⡸⠀⠀⠀⠀⠀⣸⠛⠛⠛⠓⠒⠂⠀⠀⣠⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡇⠀⠈⠂⠀⠴⠒⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⣼⠁⢣⠀⠀⢀⣀⡠⢤⠇⠀⠀⠀⠀⢰⠁⠀⠀⠀⠀⠀⣀⠤⠚⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣠⠖⠁⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⠀⠀⠉⠉⠉⠀⠀⢸⠀⠀⠀⠀⠀⠃⠀⣀⣠⠴⠒⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⢠⠊⠀⠀⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠦⠔⠒⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[0m

\033[1;31m__        _____  _     \033[1;30m_______     _____ ____  _____ ___  ____\033[0m
\033[1;31m\ \      / / _ \| |   \033[1;30m|  ___\ \   / /_ _|  _ \| ____/ _ \/ ___|\033[0m
\033[1;31m \ \ /\ / / | | | |   \033[1;30m| |_   \ \ / / | || | | |  _|| | | \___ \\ \033[0m
\033[1;31m  \ V  V /| |_| | |___\033[1;30m|  _|   \ V /  | || |_| | |__| |_| |___) |\033[0m
\033[1;31m   \_/\_/  \___/|_____\033[1;30m|_|      \_/  |___|____/|_____\___/|____/\033[0m

                         \033[1;33mby jottap_62\033[0m
""")
    print("\033[1;34m" + "="*50 + "\033[0m")
    print("\033[1;31mW\033[1;30mO\033[1;31mL\033[1;30mF \033[1;31mV\033[1;30mI\033[1;31mD\033[1;30mE\033[1;31mO\033[1;30mS   D O W N L O A D E R  4.0\033[0m")
    print("\033[1;34m" + "="*50 + "\033[0m")
    print("\033[1;36m Recursos avançados:\033[0m")
    print(" - Sistema de cookies automático")
    print(" - Bypass de restrições")
    print(" - Atualização inteligente")
    print("\033[1;34m" + "="*50 + "\033[0m")

def criar_cookies():
    """Cria arquivo de cookies padrão se não existir"""
    if not os.path.exists(ARQUIVO_COOKIES):
        cookies_padrao = """# Netscape HTTP Cookie File
.xvideos.com    TRUE    /       FALSE   1735689600      ts      1
.xvideos.com    TRUE    /       FALSE   1735689600      platform      pc
.xvideos.com    TRUE    /       FALSE   1735689600      hash    5a8d9f8e7c6b5a4d3e2f1
"""
        with open(ARQUIVO_COOKIES, 'w') as f:
            f.write(cookies_padrao)
        print("\033[1;33m[•] Arquivo de cookies criado em:", ARQUIVO_COOKIES, "\033[0m")

def verificar_dependencias():
    """Verifica e instala dependências necessárias"""
    try:
        subprocess.run(["yt-dlp", "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except:
        print("\033[1;31m[!] yt-dlp não encontrado. Instalando...\033[0m")
        subprocess.run([sys.executable, "-m", "pip", "install", "-U", "yt-dlp"], check=True)
        sleep(1)

def atualizar_ferramentas():
    """Atualiza o yt-dlp corretamente via pip"""
    print("\033[1;33m[•] Verificando atualizações...\033[0m")
    subprocess.run([sys.executable, "-m", "pip", "install", "-U", "yt-dlp"], check=True)
    sleep(1)

def baixar_video(link):
    """Executa o download com múltiplas estratégias"""
    tentativas = [
        f'yt-dlp --user-agent "{USER_AGENT}" --referer "https://www.xvideos.com" --cookies "{ARQUIVO_COOKIES}" --no-check-certificate',
        f'yt-dlp --user-agent "{USER_AGENT}" --cookies "{ARQUIVO_COOKIES}" --force-generic-extractor',
        'yt-dlp --ignore-errors --extractor-args "youtube:skip=dash"'
    ]

    for tentativa, cmd in enumerate(tentativas, 1):
        comando = f'{cmd} -f bestvideo+bestaudio/best --merge-output-format mp4 -o "{PASTA_DOWNLOADS}/%(title)s.%(ext)s" "{link}"'
        print(f"\n\033[1;35m[•] Tentativa {tentativa}/3\033[0m")

        resultado = subprocess.run(comando, shell=True)
        if resultado.returncode == 0:
            print(f"\033[1;32m[✓] Download concluído com sucesso!\033[0m")
            return True

    print("\033[1;31m[!] Todas as tentativas falharam. Verifique sua conexão e a URL.\033[0m")
    return False

def main():
    verificar_dependencias()
    criar_cookies()
    mostrar_banner()
    atualizar_ferramentas()

    while True:
        print("\n\033[1;36m[•] MENU PRINCIPAL\033[0m")
        print("1. Baixar vídeo")
        print("2. Ver formatos disponíveis")
        print("3. Atualizar cookies")
        print("4. Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "4":
            print("\033[1;32m[✓] Programa encerrado.\033[0m")
            break

        elif opcao == "3":
            criar_cookies()
            print("\033[1;32m[✓] Cookies atualizados com sucesso!\033[0m")

        elif opcao in ["1", "2"]:
            link = input("\nDigite a URL do vídeo: ").strip()

            if not link.startswith(('http://', 'https://')):
                print("\033[1;31m[!] URL inválida. Deve começar com http:// ou https://\033[0m")
                continue

            if opcao == "2":
                subprocess.run(f'yt-dlp --cookies "{ARQUIVO_COOKIES}" -F "{link}"', shell=True)
            else:
                if baixar_video(link):
                    print(f"\033[1;32m[✓] Vídeo salvo em: {PASTA_DOWNLOADS}\033[0m")
        else:
            print("\033[1;31m[!] Opção inválida. Tente novamente.\033[0m")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\033[1;31m[!] Programa interrompido pelo usuário.\033[0m")
        sys.exit(0)


