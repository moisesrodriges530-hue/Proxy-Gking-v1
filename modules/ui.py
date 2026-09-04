#!/usr/bin/env python3
from colorama import Fore, Style

class UIMenu:
    @staticmethod
    def show_menu():
        menu = f"""
{Fore.CYAN}=== MENU PRINCIPAL ==={Style.RESET_ALL}
{Fore.GREEN}1{Fore.CYAN} - Injetar HS
{Fore.GREEN}2{Fore.CYAN} - Remover HS
{Fore.GREEN}3{Fore.CYAN} - Ver Config
{Fore.GREEN}4{Fore.CYAN} - Sair
        """
        print(menu)
        return input(f"{Fore.CYAN}Opcao: {Style.RESET_ALL}").strip()
    
    @staticmethod
    def show_config(config):
        print(f"\n{Fore.CYAN}=== CONFIG ATUAL ==={Style.RESET_ALL}")
        print(f"HS Peito: {Fore.GREEN}{config.get('hs_peito')}")
        print(f"HS Pescoco: {Fore.GREEN}{config.get('hs_pescoco')}")
        print(f"HS Alto: {Fore.GREEN}{config.get('hs_alto')}")
        print(f"Antenas: {Fore.GREEN}{config.get('antena_mao_direita')}\n")