import json
import os

file_path = r"c:\Users\vaidehi koranne\OneDrive\Desktop\LangchainProject\generativeai\1-langchainintro.ipynb"

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    found = False
    for cell in nb['cells']:
        if cell.get('cell_type') == 'code':
            source = cell.get('source', [])
            # Look for the specific problematic line
            # The line in the file was "    ]\n" followed by "    config={\n"
            for i, line in enumerate(source):
                if line == "    ]\n" and (i + 1 < len(source)) and "config={" in source[i+1]:
                    source[i] = "    ],\n"
                    found = True
                    print("Found and fixed the syntax error.")
                    break
        if found:
            break

    if found:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=1)
        print("Notebook saved successfully.")
    else:
        print("Could not find the specific syntax error pattern.")

except Exception as e:
    print(f"Error: {e}")
