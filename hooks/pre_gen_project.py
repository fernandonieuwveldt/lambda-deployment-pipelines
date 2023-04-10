import sys
from cookiecutter.main import cookiecutter

# Define default values for each pipeline
lambda_function_vars = {
    "lambda_function_name": "your_default_lambda_function_name",
}

custom_layer_vars = {
    "layer_name": "your_default_layer_name",
}

lambda_function_and_layer_vars = {**lambda_function_vars, **custom_layer_vars}

container_vars = {
    "container_role_arn": "your_default_container_role_arn",
    "ecr_repository": "your_default_ecr_repo_name",
}

# Map pipeline choices to their respective variable dictionaries
pipeline_vars = {
    "lambda_function": lambda_function_vars,
    "custom_layer": custom_layer_vars,
    "both": lambda_function_and_layer_vars,
    "container": container_vars,
}

# Get the chosen pipeline from the user input
chosen_pipeline = "{{ cookiecutter.pipeline_choice }}"
print(chosen_pipeline)

# Loop through the chosen pipeline's variables
for var_name, default_value in pipeline_vars[chosen_pipeline].items():
    # Prompt the user for the required input
    user_value = input(f"Enter the value for {var_name} (default: {default_value}): ").strip()

    # Update the chosen pipeline's YAML file with the user-provided value or the default value
    yaml_file_path = f"pipelines/deploy_{chosen_pipeline}.yml"
    with open(yaml_file_path, "r") as yaml_file:
        content = yaml_file.read()

    content = content.replace(f"{{{var_name}}}", user_value or default_value)

    with open(yaml_file_path, "w") as yaml_file:
        yaml_file.write(content)
