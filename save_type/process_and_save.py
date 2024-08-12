import os
import tempfile
from datetime import datetime
import streamlit as st
from save_type.txt import save_to_txt
from save_type.excel import save_to_excel
from save_type.xml import save_to_xml
from save_type.json import save_to_json
from operation.file_operations import find_image_src

def process_and_save_data(project_dir, exclude_dirs, pattern, output_format, pattern_type):
    try:
        # Find imports
        image_imports = find_image_src(project_dir, exclude_dirs, pattern)

        # Generate a timestamp for the output file to prevent name collisions
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file_name = f'{pattern_type}_import_{timestamp}.{output_format}'
        output_file_path = os.path.join(tempfile.gettempdir(), output_file_name)

        # Save data based on the selected format
        if output_format == 'txt':
            save_to_txt(image_imports, output_file_path, pattern_type)
        elif output_format == 'json':
            save_to_json(image_imports, output_file_path, pattern_type)
        elif output_format == 'xml':
            save_to_xml(image_imports, output_file_path, pattern_type)
        elif output_format == 'excel':
            # Ensure the correct file extension for Excel
            if not output_file_path.endswith('.xlsx'):
                output_file_path = output_file_path.replace(f'.{output_format}', '.xlsx')
            save_to_excel(image_imports, output_file_path, pattern_type)

        # Read the file content to allow download
        with open(output_file_path, 'rb') as f:
            file_data = f.read()

        st.success(f'Data has been saved to {output_file_name}')
        st.download_button(
            label="Download file",
            data=file_data,
            file_name=os.path.basename(output_file_path),
            mime="application/octet-stream"
        )
    except Exception as e:
        st.error(f"An error occurred while processing the data: {e}")
        print(e)  # For debugging purposes
