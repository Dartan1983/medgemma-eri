# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY ./app /app

# Install any necessary dependencies (if any)
# RUN pip install --no-cache-dir -r requirements.txt

# Command to execute the ERI when the container starts
CMD ["python", "main.py"]
