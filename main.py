#!/usr/bin/env python3
# ============================================================
# ROOTWARE PREMIUM v3.1 - SAMPLE EDITION
# ============================================================
# This is a demonstration version for showcase purposes only.
# Full version includes dynamic exploit engine, license 
# authentication, and remote module execution capabilities.
# ============================================================
# For the complete source code and documentation, visit:
# https://rootware.pages.dev
# ============================================================

import os
import sys
import time
import platform
import getpass

RESET  = "\033[0m"
WHITE  = "\033[38;5;255m"
TEXT   = "\033[38;5;250m"
MUTED  = "\033[38;5;242m"
GREEN  = "\033[38;5;48m"
LGREEN = "\033[38;5;121m"
RED    = "\033[38;5;196m"

ROW1 = "\033[38;5;255m"
ROW2 = "\033[38;5;121m"
ROW3 = "\033[38;5;48m"

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def center(text):
    try:
        cols = os.get_terminal_size().columns
        return text.center(cols)
    except:
        return text.center(80)

def banner():
    clear()
    print("\n" * 3)
    print(center(f"{ROW1} █▀▀█ █▀▀█ █▀▀█ ▀▀█▀▀ █   █ █▀▀█ █▀▀█ █▀▀▀"))
    print(center(f"{ROW2} █▄▄▀ █  █ █  █   █   █ █ █ █▄▄█ █▄▄▀ █▀▀ "))
    print(center(f"{ROW3} █  █ ▀██▀ ▀██▀   █   ▀▄▀▄▀ █  █ █  █ █▄▄▄{RESET}"))
    print()
    print(center(f"{MUTED}[ SAMPLE EDITION - DEMONSTRATION ONLY ]{RESET}"))
    print()
    print(center(f"{GREEN}✦ rootware premium v3.1 ✦{RESET}"))
    print(center(f"{MUTED}{getpass.getuser()}@{platform.node()}  •  {platform.release()} ({platform.machine()}){RESET}"))
    print()
    print(center(f"{MUTED}For full source: https://rootware.pages.dev}"))
    print()

def menu():
    while True:
        banner()
        print(f"  {MUTED}─── workspace ───{RESET}")
        print(f"  {WHITE}[{GREEN}1{WHITE}] system info")
        print(f"  {WHITE}[{GREEN}2{WHITE}] about")
        print(f"  {WHITE}[{GREEN}3{WHITE}] exit")
        print(f"  {MUTED}─────────────────{RESET}")
        print(f"  {LGREEN}❯{RESET} ", end='')
        choice = input().strip()
        
        if choice == '1':
            banner()
            print(f"  {MUTED}─── system ───{RESET}")
            print(f"  {WHITE}user    : {GREEN}{getpass.getuser()}")
            print(f"  {WHITE}host    : {GREEN}{platform.node()}")
            print(f"  {WHITE}kernel  : {GREEN}{platform.release()}")
            print(f"  {WHITE}machine : {GREEN}{platform.machine()}")
            print(f"  {WHITE}python  : {GREEN}{sys.version.split()[0]}")
            print(f"  {MUTED}───────────────{RESET}")
            input(f"\n  {MUTED}press enter to continue{RESET}")
            
        elif choice == '2':
            banner()
            print(f"  {MUTED}─── about ───{RESET}")
            print(f"  {WHITE}rootware v3.1{RESET}")
            print(f"  {WHITE}by {GREEN}Sin7, Kize1337, God{RESET}")
            print(f"  {MUTED}supported by Zero Security & Death Networks{RESET}")
            print(f"  {MUTED}──────────────{RESET}")
            input(f"\n  {MUTED}press enter to continue{RESET}")
            
        elif choice == '3':
            print(f"\n  {MUTED}exiting...{RESET}")
            time.sleep(0.5)
            clear()
            break
        else:
            print(f"\n  {RED}invalid{RESET}")
            time.sleep(0.5)

def main():
    try:
        menu()
    except KeyboardInterrupt:
        print(f"\n\n  {MUTED}interrupted{RESET}")
        time.sleep(0.5)
        clear()

if __name__ == "__main__":
    main()
