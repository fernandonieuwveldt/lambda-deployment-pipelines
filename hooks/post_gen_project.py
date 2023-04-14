import os
import shutil


project_name = "{{ cookiecutter.project_name }}"
pipeline_choice = "{{ cookiecutter.pipeline_choice }}"
all_pipelines = ["lambda_function", "custom_layer", "lambda_function_and_layer", "lambda_container"]


def remove_dir(dir_list):
    for dir in dir_list:
        cur_dir = os.path.abspath(os.path.curdir)
        drop_dir = os.path.join(cur_dir, dir)
        if os.path.exists(drop_dir):
            shutil.rmtree(drop_dir)
        else:
            print(f"Error: The directory '{drop_dir}' could not be removed")


remove_list = [choice for choice in all_pipelines if choice != pipeline_choice]
remove_dir(
   remove_list
)
# from pathlib import Path


# project_name = "{{ cookiecutter.project_name }}"
# pipeline_choice = "{{ cookiecutter.pipeline_choice }}"
# all_pipelines = ["lambda_function", "custom_layer", "lambda_function_and_layer", "container"]


# def remove_dir(dir_list):
#     for dir in dir_list:
#         drop_dir = Path.cwd() / dir
#         if drop_dir.is_dir():
#             drop_dir.rmdir()
#         else:
#             print(f"Error: The directory '{drop_dir}' could not be removed")


# remove_list = [choice for choice in all_pipelines if choice != pipeline_choice]
# remove_dir(remove_list)
