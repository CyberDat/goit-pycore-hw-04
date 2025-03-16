import sys
import os
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)

def print_directory_structure(path: Path, indent: str = ""):
 
    if not path.exists() or not path.is_dir():
        print(Fore.RED + f"Помилка: {path} не існує або не є директорією!")
        return

    for item in path.iterdir():
        if item.is_dir():
            print(Fore.CYAN + indent + f"📂 {item.name}")
            print_directory_structure(item, indent + "  ")
        elif item.is_file():
            print(Fore.GREEN + indent + f"📜 {item.name}")

def main():
    if len(sys.argv) < 2:
        print(Fore.RED + "Помилка: необхідно вказати шлях до директорії.")
        sys.exit(1)

    dir_path = sys.argv[1]
    path = Path(dir_path)

    print_directory_structure(path)

if __name__ == "__main__":
    main()
