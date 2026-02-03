import os
import re

def file_operations(file_name, old, new):
    try:
        # current directory
        base_dir=os.path.dirname(os.path.abspath(__file__))
        file_path=os.path.join(base_dir, file_name)
        
        with open(file_path, 'r') as file:
            data= file.read()
        # case_insensitive replacing
        updated_data = re.sub(old, new, data, flags= re.IGNORECASE)
        with open(file_path, 'w') as file:
            file.write(updated_data)

        print("file updated successfully")

    except FileNotFoundError:
        print("Error: file not found, check file name")

    except PermissionError:
        print("Error: permission denied while accessing the file")

    except Exception as e:
        print(f"Unexpected error occured:{e}")

file_operations('content/sample2.txt', 'Java', 'python')
