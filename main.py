#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import json
import time
from colorama import Fore, Style, init

init(autoreset=True)

__version__ = "1.0.0"

class ProxyGking:
    def __init__(self):
        self.config = self.load_config()
        
    def load_config(self):
        try:
            with open('config.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"{Fore.RED}[x] config.json nao encontrado!")
            sys.exit(1)
    
    def show_banner(self):
        banner = f"""
{Fore.CYAN}[+] Proxy Gking v1 - Free Fire HS Injector
{Fore.GREEN}[+] by Moises Rodrigues
{Style.RESET_ALL}"""
        print(banner)
    
    def run(self):
        self.show_banner()
        print(f"{Fore.YELLOW}[*] Proxy inicializado com sucesso!")

if __name__ == "__main__":
    app = ProxyGking()
    app.run()