import pymem
import pymem.pattern
import pyuac
import sys
import os
import re
import psutil


BANNER = """
   string remover          
   by idnohwxx (milky)                     
"""

MENU = """
  ┌─────────────────────────┐
  │  1 ·  remove string     │
  │  2 ·  exit              │
  └─────────────────────────┘
"""

DIVIDER = "  " + "─" * 43


def prompt(label):
    return input(f"  ›  {label}: ")


def info(msg):
    print(f"  ·  {msg}")


def warn(msg):
    print(f"  !  {msg}")


def ok(msg):
    print(f"  >  {msg}")


def get_process_name(process_id):
    try:
        return psutil.Process(process_id).name()
    except Exception:
        return None


def remove():
    print(DIVIDER)
    try:
        string_to_remove = prompt("string to match and remove")
        if not string_to_remove:
            return

        pm = pymem.Pymem()
        pm.open_process_from_id(process_id)
        target_bytes = string_to_remove.encode("utf-8")
        pattern = re.escape(target_bytes)

        print()
        info("scanning memory ...")
        print()

        addresses = pymem.pattern.pattern_scan_all(
            pm.process_handle, pattern, return_multiple=True
        )

        if addresses:
            for addr in addresses:
                try:
                    pm.write_bytes(addr, b"\x00" * len(target_bytes), len(target_bytes))
                    ok(f"cleared  >  0x{addr:016X}")
                except Exception:
                    pass
            print()
            print(DIVIDER)
            info(f"removed {len(addresses)} instance(s).")
        else:
            print(DIVIDER)
            warn("string not found in memory.")

    except KeyboardInterrupt:
        raise
    except Exception:
        warn("an error occurred while scanning.")

    print()
    prompt("press enter to continue")


if __name__ == "__main__":
    while True:
        try:
            if not pyuac.isUserAdmin():
                print()
                warn("administrator privileges required.")
                prompt("press enter to exit")
                sys.exit(0)

            os.system("cls" if os.name == "nt" else "clear")
            print(BANNER)
            print(MENU)

            choice = prompt("choice")

            if choice == "1":
                os.system("cls" if os.name == "nt" else "clear")
                print(BANNER)

                try:
                    pid_input = prompt("target PID")
                    process_id = int(pid_input, 0)
                except ValueError:
                    warn("invalid PID.")
                    print()
                    prompt("press enter to continue")
                    continue

                process_name = get_process_name(process_id)

                if process_name:
                    print()
                    info(f"process  ·  {process_name}  [{process_id}]")
                    remove()
                else:
                    print()
                    warn(f"no process found with PID {process_id}.")
                    print()
                    prompt("press enter to continue")

            elif choice == "2":
                print()
                info("goodbye.")
                print()
                sys.exit(0)

            else:
                print()
                warn("invalid choice — try again.")
                print()

        except KeyboardInterrupt:
            print()
            print()
            info("goodbye.")
            print()
            sys.exit(0)