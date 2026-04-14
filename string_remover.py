import pymem
import pymem.pattern
import pyuac
import sys
import os
import re

def remove():
    try:
        string_to_remove = input("[>] " + "enter string to match and remove: ")
        if not string_to_remove:
            return

        pm = pymem.Pymem()
        pm.open_process_from_id(process_id)
        target_bytes = string_to_remove.encode('utf-8')
        pattern = re.escape(target_bytes)
        
        print("[>] " + "scanning memory...")
        addresses = pymem.pattern.pattern_scan_all(pm.process_handle, pattern, return_multiple=True)

        if addresses:
            for addr in addresses:
                try:
                    pm.write_bytes(addr, b'\x00' * len(target_bytes), len(target_bytes))
                    print("[>] " + f"{addr} has been deleted")
                except Exception:
                    pass
            print("[>] " + f"removed {len(addresses)} instances.")
        else:
            print("[>] " + "string not found!")
    except KeyboardInterrupt:
        raise
    except Exception:
        print("[>] " + "string error!")


if __name__ == "__main__":
    try:
        if not pyuac.isUserAdmin():
            input("[!] " + "please run as admin. press enter to continue...")
            sys.exit(0)

        os.system('cls')
        print("[>] " + "made by idnohwxx (milky)\n")
        print("[>] " + "1. " + "remove string")
        print("[>] " + "2. " + "exit\n")
        choice = input("[>] " + "enter your choice: ")
        if choice == "1":
            os.system('cls')
            process_id = int(input("[>] " + "Enter PID: "), 0)
            remove()
        elif choice == "2":
            print("\n" + "[>] " + "goodbye!")
            sys.exit(0)
        else:
            print("[>] " + "invalid choose. try again.\n")
        while True:
            remove()
    except KeyboardInterrupt:
        print("\n" + "[>] " + "goodbye!")
        sys.exit(0)
