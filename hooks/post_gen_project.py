import shutil
from pathlib import Path


project_name = "{{ cookiecutter.project_name }}"
pipeline_choice = "{{ cookiecutter.pipeline_choice }}"
all_pipelines = ["lambda_function", "custom_layer", "lambda_function_and_layer", "lambda_container"]


def remove_dir(dir_list):
    for dir in dir_list:
        drop_dir = Path.cwd() / dir
        if drop_dir.exists():
            shutil.rmtree(drop_dir)
        else:
            print(f"Error: The directory '{drop_dir}' could not be removed")


remove_list = [choice for choice in all_pipelines if choice != pipeline_choice]
remove_dir(remove_list)
