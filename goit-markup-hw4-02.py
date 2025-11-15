import os
from typing import List, Dict, Any

def get_cats_info(path: str) -> List[Dict[str, str]]:
    
    cats_list = []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cleaned_line = line.strip()
                
                if not cleaned_line:
                    continue
                parts = cleaned_line.split(',')
                
                if len(parts) == 3:
                    cat_id, name, age = parts
                    
                    cat_dict = {
                        "id": cat_id,
                        "name": name,
                        "age": age
                    }

                    cats_list.append(cat_dict)
                else:
                    print(f"Warning: Row skipped: {cleaned_line}")
                    
    except FileNotFoundError:
        print(f"Error: File at path '{path}' not found.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
        return []

    return cats_list

cats_info = get_cats_info(r"C:\Users\renew\OneDrive\Документы\Go IT\HW4\goit-pycore-hw-04\cats_file.txt")
print(cats_info)
