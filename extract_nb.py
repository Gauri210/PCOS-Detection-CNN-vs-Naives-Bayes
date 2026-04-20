import json
import sys

def extract_content(notebook_path, output_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        for i, cell in enumerate(nb.get('cells', [])):
            cell_type = cell.get('cell_type')
            source = "".join(cell.get('source', []))
            
            if cell_type == 'markdown':
                f.write(f"--- Markdown Cell {i} ---\n{source}\n\n")
            elif cell_type == 'code':
                f.write(f"--- Code Cell {i} ---\n{source}\n\n")

if __name__ == '__main__':
    extract_content('IDSA_Project_Final.ipynb', 'nb_content.txt')
