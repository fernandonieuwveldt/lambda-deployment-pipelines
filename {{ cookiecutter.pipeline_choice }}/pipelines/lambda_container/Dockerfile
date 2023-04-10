# Use AWS-provided base image for Python
FROM public.ecr.aws/lambda/python:3.9

# Copy function code and dependencies
COPY container/app.py ${LAMBDA_TASK_ROOT}
COPY requirements.txt ./

# Install dependencies
RUN pip install -r requirements.txt

# Set the CMD to your handler (replace `app.lambda_handler` with your specific handler)
CMD ["app.lambda_handler"]
