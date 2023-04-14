# # import os
# # import shutil
# # import sys

# # def prompt_user(prompt):
# #     try:
# #         return sys.raw_input(prompt)
# #     except NameError:
# #         return input(prompt)

# # pipelines_dir = 'pipelines'
# # choices = {
# #     'lambda_function': 'pipelines/lambda_function/deploy_lambda_function.yml',
# #     'custom_layer': 'pipelines/custom_layer/deploy_custom_layer.yml',
# #     'lambda_function_and_layer': 'pipelines/lambda_function_and_layer/deploy_lambda_function_and_layer.yml',
# #     'container': 'pipelines/lambda_container/deploy_lambda_container.yml'
# # }

# # pipeline_choice = '{{ cookiecutter.pipeline_choice }}'
# # lambda_function_name = "test_function"  # prompt_user("Enter the Lambda function name: ")

# # # Prompt the user for required values based on the chosen pipeline
# # # if pipeline_choice == "lambda_function":
# # #     lambda_function_name = prompt_user("Enter the Lambda function name: ")
# # # elif pipeline_choice == "custom_layer":
# # #     role_arn = prompt_user("Enter the custom layer role ARN: ")
# # # elif pipeline_choice == "both":
# # #     role_arn = prompt_user("Enter the role ARN for both Lambda function and custom layer: ")
# # # else:
# # #     role_arn = prompt_user("Enter the role ARN for the Lambda container: ")
# # #     ecr_repository = prompt_user("Enter the ECR repository name: ")

# # # Update the chosen pipeline's YAML file with the user-provided values
# # src = os.path.join(pipelines_dir, choices[pipeline_choice])
# # # dst = os.path.join('{{ cookiecutter.pipeline_choice }}', os.path.basename(src))
# # dst = os.path.join(pipeline_choice, os.path.basename(src))

# # print("src", src)
# # print("dst", dst)

# # with open(dst, 'wt') as f_dst:  #open(src, 'rt') as f_src: # , open(dst, 'wt') as f_dst:
# #     for line in [0,1]:
# #         # f_dst.write(line.replace('{{ cookiecutter.lambda_function_name }}', lambda_function_name))
# #         print("ddd")

# import os
# import shutil
# import sys

# def prompt_user(prompt):
#     try:
#         return sys.raw_input(prompt)
#     except NameError:
#         return input(prompt)

# root_dir = os.path.dirname(os.path.abspath(__file__))
# pipelines_dir = os.path.join(root_dir, 'pipelines')
# choices = {
#     'lambda_function': 'pipelines/lambda_function/deploy_lambda_function.yml',
#     'custom_layer': 'pipelines/custom_layer/deploy_custom_layer.yml',
#     'both': 'pipelines/lambda_function_and_layer/deploy_lambda_function_and_layer.yml',
#     'container': 'pipelines/lambda_container/deploy_lambda_container.yml'
# }

# pipeline_choice = '{{ cookiecutter.pipeline_choice }}'
# lambda_function_name = "test_function"  # prompt_user("Enter the Lambda function name: ")

# # Update the chosen pipeline's YAML file with the user-provided values
# src = os.path.join(root_dir, choices[pipeline_choice])

# # Ensure the destination directory exists
# dst_dir = os.path.join(root_dir, '{{ cookiecutter.pipeline_choice }}')
# os.makedirs(dst_dir, exist_ok=True)
# dst = os.path.join(dst_dir, os.path.basename(src))

# print("src", src)
# print("dst", dst)

# with open(src, 'rt') as f_src, open(dst, 'wt') as f_dst:
#     for line in f_src:
#         f_dst.write(line.replace('{{ cookiecutter.lambda_function_name }}', lambda_function_name))
# import os
# import shutil
# import sys

# def prompt_user(prompt):
#     try:
#         return sys.raw_input(prompt)
#     except NameError:
#         return input(prompt)

# template_dir = '{{ cookiecutter._template }}'
# pipelines_dir = os.path.join(template_dir, 'pipelines')
# choices = {
#     'lambda_function': 'pipelines/lambda_function/deploy_lambda_function.yml',
#     'custom_layer': 'pipelines/custom_layer/deploy_custom_layer.yml',
#     'both': 'pipelines/lambda_function_and_layer/deploy_lambda_function_and_layer.yml',
#     'container': 'pipelines/lambda_container/deploy_lambda_container.yml'
# }

# pipeline_choice = '{{ cookiecutter.pipeline_choice }}'
# lambda_function_name = "test_function"  # prompt_user("Enter the Lambda function name: ")

# # Update the chosen pipeline's YAML file with the user-provided values
# src = os.path.join(template_dir, choices[pipeline_choice])

# # Ensure the destination directory exists
# dst_dir = os.path.join('{{ cookiecutter.pipeline_choice }}')
# os.makedirs(dst_dir, exist_ok=True)
# dst = os.path.join(dst_dir, os.path.basename(src))

# print("src", src)
# print("dst", dst)

# with open(src, 'rt') as f_src, open(dst, 'wt') as f_dst:
#     for line in f_src:
#         f_dst.write(line.replace('{{ cookiecutter.lambda_function_name }}', lambda_function_name))

# import os
# import requests
# import sys

# def prompt_user(prompt):
#     try:
#         return sys.raw_input(prompt)
#     except NameError:
#         return input(prompt)

# github_base_url = 'https://raw.githubusercontent.com/your_username/your_repository/feature/pipelines-as-modules/'
# choices = {
#     'lambda_function': 'pipelines/lambda_function/deploy_lambda_function.yml',
#     'custom_layer': 'pipelines/custom_layer/deploy_custom_layer.yml',
#     'both': 'pipelines/lambda_function_and_layer/deploy_lambda_function_and_layer.yml',
#     'container': 'pipelines/lambda_container/deploy_lambda_container.yml'
# }

# pipeline_choice = '{{ cookiecutter.pipeline_choice }}'
# lambda_function_name = "test_function"  # prompt_user("Enter the Lambda function name: ")

# # Get the chosen pipeline's YAML file from the GitHub repository
# src_url = github_base_url + choices[pipeline_choice]
# response = requests.get(src_url)

# if response.status_code == 200:
#     # Ensure the destination directory exists
#     dst_dir = os.path.join('{{ cookiecutter.pipeline_choice }}')
#     os.makedirs(dst_dir, exist_ok=True)
#     dst = os.path.join(dst_dir, os.path.basename(choices[pipeline_choice]))

#     print("src_url", src_url)
#     print("dst", dst)

#     with open(dst, 'wt') as f_dst:
#         for line in response.text.splitlines():
#             f_dst.write(line.replace('{{ cookiecutter.lambda_function_name }}', lambda_function_name) + '\n')
# else:
#     print(f"Error: Unable to download the file. Status code: {response.status_code}")

import os
import sys

def prompt_user(prompt):
    try:
        return sys.raw_input(prompt)
    except NameError:
        return input(prompt)

template_dir = '{{ cookiecutter._template }}'
choices = {
    'lambda_function': '{{cookiecutter.pipeline_choice}}/pipelines/lambda_function/deploy_lambda_function.yml',
    'custom_layer': '{{cookiecutter.pipeline_choice}}/pipelines/custom_layer/deploy_custom_layer.yml',
    'both': '{{cookiecutter.pipeline_choice}}/pipelines/lambda_function_and_layer/deploy_lambda_function_and_layer.yml',
    'container': '{{cookiecutter.pipeline_choice}}/pipelines/lambda_container/deploy_lambda_container.yml'
}

pipeline_choice = '{{ cookiecutter.pipeline_choice }}'
lambda_function_name = "test_function"  # prompt_user("Enter the Lambda function name: ")

# Update the chosen pipeline's YAML file with the user-provided values
src = os.path.join(template_dir, choices[pipeline_choice])

# Ensure the destination directory exists
dst_dir = os.path.join('{{ cookiecutter.pipeline_choice }}')
os.makedirs(dst_dir, exist_ok=True)
dst = os.path.join(dst_dir, os.path.basename(src))

print("src", src)
print("dst", dst)

with open(src, 'rt') as f_src, open(dst, 'wt') as f_dst:
    for line in f_src:
        f_dst.write(line.replace('{{ cookiecutter.lambda_function_name }}', lambda_function_name))
