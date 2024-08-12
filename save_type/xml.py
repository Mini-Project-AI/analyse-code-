import dicttoxml
import os

def save_to_xml(image_imports, output_file, type):
    # Ensure the output directory exists
    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Prepare the data for XML conversion
    output_data = {'files': []}
    for file, imports in image_imports.items():
        file_data = {'path': file, 'imports': []}
        for imp in imports:
            if len(imp) == 2:  # For MUI icons
                file_data['imports'].append({'type': type, 'name': imp[1]})
            else:  # For images
                file_data['imports'].append({'type': type, 'name': imp[0], 'path': f'/public/{imp[1]}'})
        output_data['files'].append(file_data)
    
    # Convert the dictionary to XML
    xml_data = dicttoxml.dicttoxml(output_data)

    # Write XML data to file
    with open(output_file, 'wb') as f:
        f.write(xml_data)
