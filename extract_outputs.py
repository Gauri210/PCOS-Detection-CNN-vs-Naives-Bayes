import json
import base64
import os

def extract_outputs(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    img_count = 0
    with open('extracted_text_outputs.txt', 'w', encoding='utf-8') as out_f:
        for i, cell in enumerate(nb.get('cells', [])):
            if cell.get('cell_type') == 'code':
                outputs = cell.get('outputs', [])
                if outputs:
                    out_f.write(f"--- Cell {i} Outputs ---\n")
                
                for output in outputs:
                    output_type = output.get('output_type')
                    
                    if output_type == 'stream':
                        text = "".join(output.get('text', []))
                        out_f.write(text + "\n")
                    
                    elif output_type in ['display_data', 'execute_result']:
                        data = output.get('data', {})
                        
                        # Extract text
                        if 'text/plain' in data:
                            text = "".join(data['text/plain'])
                            out_f.write(text + "\n")
                            
                        # Extract images
                        if 'image/png' in data:
                            img_data = base64.b64decode(data['image/png'])
                            img_filename = f'graph_cell_{i}_{img_count}.png'
                            with open(img_filename, 'wb') as img_f:
                                img_f.write(img_data)
                            out_f.write(f"[Extracted Image saved as {img_filename}]\n")
                            img_count += 1

if __name__ == '__main__':
    extract_outputs('IDSA_Project_Final.ipynb')
    print("Done extracting outputs.")
