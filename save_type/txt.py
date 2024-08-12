import os

def save_to_txt(image_imports, output_file, type):
    # Ensure the output directory exists
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(output_file, 'w', encoding='utf-8') as f:
        for file, imports in image_imports.items():
            f.write(f'File: {file}\n')
            f.write('-' * 50 + '\n')  # Separator for better readability
            for imp in imports:
                if len(imp) == 2:  # For MUI icons
                    f.write(f'  {type}: {imp[1]} -> /public/{imp[1]}\n')
                else:  # For images
                    f.write(f'  {type}: {imp[0]} -> /public/{imp[1]}\n')
            f.write('\n')  # Blank line between files
            f.write('=' * 50 + '\n')  # Separator between files
    pass