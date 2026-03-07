import os
import time

def design():
    os.system('clear')
    print("\033[1;35m      ______")
    print("     //  ||\\ \\")
    print("  ____//___||_\\ \\___")
    print(" )  _          _    \\")
    print(" |_/ \________/ \___|")
    print("   \_/        \_/    \033[0m")
    print("\033[1;34m  _   _  _____  _   _  ____  ___ ")
    print(" | \ | || ____|| | | ||  _ \|_ _|")
    print(" |  \| ||  _|  | |_| || | | || | ")
    print(" | |\  || |___ |  _  || |_| || | ")
    print(" |_| \_||_____||_| |_||____/|___|\033[0m")
    print("\n\033[1;32m[ MEHDI ]\033[0m \033[1;33m—\033[0m \033[1;32m[ TikTok Tool ]\033[0m")
    print("-----------------------------------")

def menu():
    design()
    print("\033[1;31m[01]\033[0m Increase Followers")
    print("\033[1;31m[02]\033[0m Increase Likes")
    print("\033[1;31m[03]\033[0m Video Views")
    print("\033[1;31m[00]\033[0m Exit")
    print("-----------------------------------")

menu()
choice = input("\033[1;32m⚔️ Choose an option: \033[0m")

if choice in ['1', '2', '3']:
    user = input("\033[1;32m⚔️ Enter TikTok Username: \033[0m")
    print(f"\n[!] Connecting to @{user}...")
    time.sleep(2)
    print("\033[1;31m[X] Error: Request Blocked by TikTok Firewall.\033[0m")
else:
    print("Exiting...")
