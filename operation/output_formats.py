import importlib
def save_data(data, output_type, output_file):
    # Dictionary mapping output types to their corresponding module and function names
    save_functions = {
        'txt': 'save_type.txt.save_to_txt',
        'json': 'save_type.json.save_to_json',
        'xml': 'save_type.xml.save_to_xml',
        'excel': 'save_type.excel.save_to_excel'
    }
    
    # Get the function path based on the output_type
    function_path = save_functions.get(output_type)
    if function_path:
        module_name, func_name = function_path.rsplit('.', 1)
        module = importlib.import_module(module_name)
        save_function = getattr(module, func_name)
        save_function(data, output_file)
    else:
        raise ValueError(f"Invalid output type: {output_type}. Available types are: {', '.join(save_functions.keys())}")