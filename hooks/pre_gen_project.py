import os
import sys

def prompt_user(prompt):
    try:
        return sys.raw_input(prompt)
    except NameError:
        return input(prompt)

choices = {
    'lambda_function': 'pipelines/lambda_function/deploy_lambda_function.yml',
    'custom_layer': 'pipelines/custom_layer/deploy_custom_layer.yml',
    'both': 'pipelines/lambda_function_and_layer/deploy_lambda_function_and_layer.yml',
    'container': 'pipelines/lambda_container/deploy_lambda_container.yml'
}

pipeline_choice = '{{ cookiecutter.pipeline_choice }}'
lambda_function_name = "test_function"  # prompt_user("Enter the Lambda function name: ")

# Update the chosen pipeline's YAML file with the user-provided values
src = choices[pipeline_choice]

# Ensure the destination directory exists
dst_dir = os.path.join('{{ cookiecutter.pipeline_choice }}')
os.makedirs(dst_dir, exist_ok=True)
dst = os.path.join(dst_dir, os.path.basename(src))

print("src", src)
print("dst", dst)

with open(src, 'rt') as f_src, open(dst, 'wt') as f_dst:
    for line in f_src:
        f_dst.write(line.replace('{{ cookiecutter.lambda_function_name }}', lambda_function_name))
