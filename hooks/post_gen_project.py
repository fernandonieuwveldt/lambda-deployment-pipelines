import json
import os
import sys

cookiecutter_json_file = os.path.join(os.path.dirname(__file__), '..', 'cookiecutter.json')

def read_json_file(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def write_json_file(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

def update_cookiecutter_json(pipeline_choice):
    cookiecutter_data = read_json_file(cookiecutter_json_file)

    default_values = {
        'custom_layer': {
            'layer_name': 'example_layer'
        },
        'lambda_container': {
            'container_name': 'example_container'
        },
        'lambda_function': {
            'function_name': 'example_function'
        },
        'lambda_function_and_layer': {
            'function_name': 'example_function',
            'layer_name': 'example_layer'
        }
    }

    for key, value in default_values[pipeline_choice].items():
        cookiecutter_data[key] = value

    write_json_file(cookiecutter_json_file, cookiecutter_data)

pipeline_choice = "{{ cookiecutter.pipeline_choice }}"

if pipeline_choice not in ['custom_layer', 'lambda_container', 'lambda_function', 'lambda_function_and_layer']:
    print(f"ERROR: Invalid pipeline choice '{pipeline_choice}'.")
    sys.exit(1)

update_cookiecutter_json(pipeline_choice)
