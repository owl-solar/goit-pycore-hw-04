
import sys                          
from pathlib import Path
from typing import Optional            
from colorama import Fore, Style, init  

init(autoreset=True)

def get_system_structure(directory: Path, prefix: str = ""):
    if prefix == "":
        print(Fore.BLUE + directory.name + "/" + Style.RESET_ALL)
    
    try:
        items = sorted(directory.iterdir(), key=lambda x: (x.is_file(), x.name.lower()))
    except PermissionError:
        print(prefix + Fore.RED + "Access denied" + Style.RESET_ALL)
        return

    for i, item in enumerate(items):
        is_last = (i == len(items) - 1) 
        connector = '└─' if is_last else '├─' 
        extension = "    " if is_last else "|   " 

        if item.is_dir():
            print(Fore.BLUE + prefix + connector + item.name + "/")
            get_system_structure(item, prefix + extension)
        else: # If current item is a file
            print(Fore.GREEN + prefix + connector + item.name)

target_path = Path(sys.argv[1]).resolve() 

if not target_path.exists():
    print(Fore.RED + f"Error: Path '{target_path}' does not exist." + Style.RESET_ALL)
    sys.exit(1)

if not target_path.is_dir(): 
    print(Fore.RED + f"Error: '{target_path}' is not a directory." + Style.RESET_ALL)
    sys.exit(1)

get_system_structure(target_path)              