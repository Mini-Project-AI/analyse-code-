import sys

def print_help():
    help_message = """
Usage: python collect_data.py <pattern_type> <output_format>

This script scans through a project directory to find image and icon imports based on the specified pattern type. It then saves the results in the specified output format.

Arguments:
  <pattern_type>   The type of import pattern to search for. Available types:
                   - svg: To find imports of SVG files.
                   - image: To find imports of PNG, JPG, or JPEG files.
                   - mui_icon: To find imports of Material-UI icons.

  <output_format>  The format to save the results. Available formats:
                   - txt: Save results as a plain text file.
                   - json: Save results as a JSON file.
                   - xml: Save results as an XML file.
                   - excel: Save results as an Excel file.

Options:
  --help           Show this help message and exit.

Example:
  python collect_data.py image json
  This command will search for image imports in the project directory and save the results in a JSON file.

Notes:
  - Ensure that the output directory for the specified format exists or will be created automatically.
  - The script excludes common directories like node_modules and assets by default. Modify these settings if necessary.

Output Format Details:

1. **Text (`txt`)**:
   - Saves results in a plain text file.
   - Each file's imports are listed with their types and paths.
   - File paths and types are clearly separated for readability.

2. **JSON (`json`)**:
   - Saves results in a JSON file.
   - The JSON structure includes file paths as keys with an array of import details.
   - Each import detail includes the type and additional attributes like name and path.

3. **XML (`xml`)**:
   - Saves results in an XML file.
   - Uses a root element `<root>` with each file's imports contained within.
   - Each import detail is represented with appropriate XML tags.

4. **Excel (`excel`)**:
   - Saves results in an Excel file.
   - Creates a table with columns for file paths, import types, names, and paths.
   - Useful for data analysis or reporting in a tabular format.

For more details, refer to the documentation or contact the script author.
"""
    print(help_message)
    sys.exit(0)
