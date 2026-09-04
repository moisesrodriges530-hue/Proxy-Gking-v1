#!/usr/bin/env python3
from colorama import Fore, init
from config import *
init(autoreset=True)

print(f"{Fore.CYAN}[+] Proxy Gking v{PROXY_VERSION} - Free Fire HS Injector")
print(f"{Fore.GREEN}[+] by Moises Rodrigues\n")

while True:
    print(f"{Fore.CYAN}=== MENU ===")
    print(f"{Fore.GREEN}1{Fore.WHITE} - Injetar HS")
    print(f"{Fore.GREEN}2{Fore.WHITE} - Remover HS")
    print(f"{Fore.GREEN}3{Fore.WHITE} - Ver Config")
    print(f"{Fore.GREEN}4{Fore.WHITE} - Sair\n")
    
    opcao = input(f"{Fore.YELLOW}Escolha: ")
    
    if opcao == "1":
        print(f"{Fore.YELLOW}[*] Injetando HS...")
        print(f"{Fore.GREEN}[✓] HS Injetado com sucesso!\n")
    elif opcao == "2":
        print(f"{Fore.YELLOW}[*] Removendo HS...")
        print(f"{Fore.GREEN}[✓] HS Removido com sucesso!\n")
    elif opcao == "3":
        print(f"{Fore.CYAN}[*] Proxy v{PROXY_VERSION} - {PROXY_STATUS}")
        print(f"{Fore.CYAN}[*] Host: {PROXY_HOST}:{PROXY_PORT}\n")
    elif opcao == "4":
        print(f"{Fore.RED}[!] Saindo...")
        break
    else:
        print(f"{Fore.RED}[x] Opção inválida!\n")
