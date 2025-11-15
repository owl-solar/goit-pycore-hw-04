import os
from typing import Tuple

def total_salary(path: str) -> Tuple[float, float]:
    
    total_sum = 0.0
    developer_count = 0
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cleaned_line = line.strip()
                
                if not cleaned_line:
                    continue
                
                try:
                    parts = cleaned_line.split(',', 1)
                    if len(parts) < 2:
                        print(f"Warning: Skipping line due to insufficient data: {cleaned_line}")
                        continue
                        
                    salary_str = parts[1]
                    
                    salary = float(salary_str)
                    
                    total_sum += salary
                    developer_count += 1
                
                except ValueError:
                    print(f"Warning: Skipping line due to non-numeric salary value: {cleaned_line}")
                    continue
                    
    except FileNotFoundError:
        print(f"Error: The file at path '{path}' was not found.")
        return (0.0, 0.0)
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
        return (0.0, 0.0)

    average_salary = total_sum / developer_count if developer_count > 0 else 0.0

    return (total_sum, average_salary)

total, average = total_salary(r"C:\Users\renew\OneDrive\Документы\Go IT\HW4\goit-pycore-hw-04\salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
