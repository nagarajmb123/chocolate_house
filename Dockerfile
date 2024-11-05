# Dockerfile
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy the project files
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Initialize the database
RUN python models/db_setup.py

# Run the application
CMD ["python", "app.py"]
