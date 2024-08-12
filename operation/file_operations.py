import os
import re

def find_image_src(project_dir, exclude_dirs, pattern):
    image_imports = {}

    for root, dirs, files in os.walk(project_dir):
        # Exclude directories
        dirs[:] = [d for d in dirs if os.path.abspath(os.path.join(root, d)) not in exclude_dirs]

        for file in files:
            if file.endswith(('.js', '.jsx', '.ts', '.tsx')):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                except UnicodeDecodeError:
                    with open(file_path, 'r', encoding='latin-1') as f:
                        content = f.read()
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")
                    continue

                matches = pattern.findall(content)
                if matches:
                    # Convert file_path to be relative to project_dir
                    rel_file_path = os.path.relpath(file_path, project_dir)
                    # Update matches to use relative paths if necessary
                    relative_matches = [(name, os.path.relpath(path, project_dir)) for name, path in matches]
                    image_imports[rel_file_path] = relative_matches

    return image_imports
