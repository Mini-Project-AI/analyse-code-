import os
import json

def save_to_json(image_imports, output_file, type):
    # Ensure the output directory exists
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_data = {}
    for file, imports in image_imports.items():
        output_data[file] = []
        for imp in imports:
            if len(imp) == 2:  # For MUI icons
                output_data[file].append({'type': type, 'name': imp[1]})
            else:  # For images
                output_data[file].append({'type': type, 'name': imp[0], 'path': f'/public/{imp[1]}'})
    
    # Write JSON data to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=4, ensure_ascii=False)

    print(f"Data has been saved to {output_file}")
