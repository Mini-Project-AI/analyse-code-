import streamlit as st
import os
from utils.extract_zip import extract_zip
from save_type.process_and_save import process_and_save_data
import re

# Define the patterns for different types of imports
PATTERNS = {
    'svg': re.compile(r'import\s+(\w+)\s+from\s+\'([^\']+\.svg)\''),
    'image': re.compile(r'import\s+(\w+)\s+from\s+\'([^\']+\.png|jpg|jpeg)\''),
    'icon': re.compile(r'import\s+(\w+)\s+from\s+\'@mui/icons-material/(\w+)\'')
}

def import_finder_exporter_view():
    st.title('Import Finder and Exporter')

    # Upload file input
    uploaded_file = st.file_uploader("Upload a ZIP file containing the project", type="zip")

    # User input for pattern type and output format
    pattern_type = st.selectbox('Select import pattern type:', list(PATTERNS.keys()))
    output_format = st.selectbox('Select output format:', ['txt', 'json', 'xml', 'excel'])

    if not uploaded_file:
        project_dir = st.text_input('Project Directory', '../../bmft')
        exclude_dirs_input = st.text_area('Directories to Exclude (comma-separated)', '/node_modules, /src/assets')
        exclude_dirs = [os.path.abspath(d.strip()) for d in exclude_dirs_input.split(',')]
    else:
        # Extract the uploaded zip file
        project_dir = extract_zip(uploaded_file)
        exclude_dirs = []

    if st.button('Run'):
        if not os.path.isdir(project_dir):
            st.error("The specified project directory does not exist.")
            return

        pattern = PATTERNS.get(pattern_type)
        if not pattern:
            st.error("Invalid pattern type selected.")
            return

        # Process and save the data
        process_and_save_data(project_dir, exclude_dirs, pattern, output_format, pattern_type)
