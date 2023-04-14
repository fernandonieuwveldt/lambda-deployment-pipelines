import os
import shutil
import sys

pipeline_choice = "{{ cookiecutter.pipeline_choice }}"

if pipeline_choice not in ['custom_layer', 'lambda_container', 'lambda_function', 'lambda_function_and_layer']:
    print(f"ERROR: Invalid pipeline choice '{pipeline_choice}'.")
    sys.exit(1)

source_directory = os.path.join('{{cookiecutter.pipeline_choice}}', 'pipelines', pipeline_choice)
destination_directory = '.'

for file in os.listdir(source_directory):
    if file.endswith('.yml'):
        shutil.copy2(os.path.join(source_directory, file), destination_directory)

shutil.rmtree('{{cookiecutter.pipeline_choice}}')
