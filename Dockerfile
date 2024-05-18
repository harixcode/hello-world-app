# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Install Tkinter
RUN apt-get update && apt-get install -y python3-tk

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Run the application
CMD ["python", "app.py"]
