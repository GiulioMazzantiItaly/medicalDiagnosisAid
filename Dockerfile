# Use a lightweight official Python 3.12 image as the base environment
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only the dependency list first to take advantage of Docker layer caching
COPY requirements.txt .

# Install all Python dependencies without keeping pip cache files
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files into the container
COPY . .

# Document that the application uses port 5000
EXPOSE 5000

# Start the Flask application when the container runs
CMD ["python", "app.py"]