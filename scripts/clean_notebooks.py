import nbformat
import os

def clean_notebook(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    # 1. Clear outputs and reset execution counts
    # 2. Remove empty cells
    new_cells = []
    for cell in nb.cells:
        if cell.cell_type == 'code':
            cell.outputs = []
            cell.execution_count = None
        
        # Check if cell is not empty
        if cell.source.strip():
            new_cells.append(cell)
    
    nb.cells = new_cells

    with open(file_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    print(f"Cleaned: {file_path}")

def main():
    for root, dirs, files in os.walk('.'):
        if '.venv' in dirs:
            dirs.remove('.venv')
        if '.git' in dirs:
            dirs.remove('.git')
        
        for file in files:
            if file.endswith('.ipynb'):
                clean_notebook(os.path.join(root, file))

if __name__ == "__main__":
    main()
