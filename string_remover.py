import pymem
import pyuac
from colorama import init, Fore
import sys
import os
# Initialising Colorama
init()


def remove():
    try:
        string_to_removed = input(Fore.LIGHTCYAN_EX + "[?] " + Fore.LIGHTWHITE_EX + "Enter Strings: ")
        address = int(string_to_removed.split()[0], 0)
        length = int(string_to_removed.split("(")[1].split(")")[0], 0)

        pymem.memory.write_string(pymem.process.open(process_id), address, bytes(length))
        print(Fore.LIGHTGREEN_EX + "[+] " + Fore.LIGHTWHITE_EX + "string removed..")
    except KeyboardInterrupt:
        raise
    except Exception:
        print(Fore.LIGHTRED_EX + "[-] " + Fore.LIGHTWHITE_EX + "string error!")


if __name__ == "__main__":
    try:
        if not pyuac.isUserAdmin():
            input(Fore.LIGHTYELLOW_EX + "[!] " + Fore.LIGHTWHITE_EX + "Please run as admin. Press Enter to continue...")
            sys.exit(0)
        os.system('cls')
        print(Fore.LIGHTCYAN_EX + "[*] " + Fore.LIGHTWHITE_EX + "made by idnohwxx (milky)\n")
        print(Fore.LIGHTYELLOW_EX + "[*] " + Fore.LIGHTWHITE_EX + "1. " + Fore.LIGHTWHITE_EX + "remove string")
        print(Fore.LIGHTYELLOW_EX + "[*] " + Fore.LIGHTWHITE_EX + "2. " + Fore.LIGHTWHITE_EX + "exit\n")
        choice = input(Fore.LIGHTCYAN_EX + "[?] " + Fore.LIGHTWHITE_EX + "Enter your choice: ")
        if choice == "1":
            os.system('cls')
            process_id = int(input(Fore.LIGHTCYAN_EX + "[?] " + Fore.LIGHTWHITE_EX + "Enter PID: "), 0)
            remove()
        elif choice == "2":
            print("\n" + Fore.LIGHTCYAN_EX + "[*] " + Fore.LIGHTWHITE_EX + "Goodbye!")
            sys.exit(0)
        else:
            print(Fore.LIGHTRED_EX + "[-] " + Fore.LIGHTWHITE_EX + "invalid choose. try again.\n")
        while True:
            remove()
    except KeyboardInterrupt:
        print("\n" + Fore.LIGHTCYAN_EX + "[*] " + Fore.LIGHTWHITE_EX + "Goodbye!")
        sys.exit(0)
