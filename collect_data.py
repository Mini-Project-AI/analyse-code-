import os
import sys
import importlib
import re
from operation.file_operations import find_image_src
from operation.output_formats import save_data
from utils.help_utils import print_help
from save_type.txt import save_to_txt
from save_type.excel import save_to_excel
from save_type.xml import save_to_xml
from save_type.json import save_to_json

PATTERNS = {
    'svg': re.compile(r'import\s+(\w+)\s+from\s+\'([^\']+\.svg)\''),
    'image': re.compile(r'import\s+(\w+)\s+from\s+\'([^\']+\.png|jpg|jpeg)\''),
    'icon': re.compile(r'import\s+(\w+)\s+from\s+\'@mui/icons-material/(\w+)\'')
}

project_dir = '../../bmft'  # Replace with your project path
exclude_dirs = [
    os.path.abspath('../../bmft/node_modules'),  # Node modules directory
    os.path.abspath('../../bmft/src/assets'),     # Assets directory
]

save_funcs = {
    'txt': save_to_txt,
    'json': save_to_json,
    'xml': save_to_xml,
    'excel': save_to_excel
}

def main():
    if len(sys.argv) != 3:
        print_help()

    pattern_type = sys.argv[1]
    output_format = sys.argv[2]
    if pattern_type not in PATTERNS:
        print(f"Invalid pattern type. Available types: {', '.join(PATTERNS.keys())}")
        sys.exit(1)
    if output_format not in ['txt', 'json', 'xml', 'excel']:
        print(f"Invalid output format. Available formats: txt, json, xml, excel")
        sys.exit(1)

    output_file = f'output/{pattern_type}/{pattern_type}_import.{output_format}'
    
    if output_format == 'excel' and not output_file.lower().endswith('.xlsx'):
        output_file += '.xlsx'

    print(f"Project directory: {project_dir}")
    print(f"Excluding directories: {exclude_dirs}")

    pattern = PATTERNS[pattern_type]

    image_imports = find_image_src(project_dir, exclude_dirs, pattern)
    
    save_func = save_funcs[output_format]
    save_func(image_imports, output_file, sys.argv[1])

    print(f'Image imports have been saved to {output_file}')

if __name__ == "__main__":
    main()
