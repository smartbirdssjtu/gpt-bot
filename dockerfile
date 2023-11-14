# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install system-level dependencies (if any)
RUN apt-get update && \
    apt-get install -y procps && \
    apt-get install -y iproute2 && \
    rm -rf /var/lib/apt/lists/*

RUN 

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Create a non-root user
RUN useradd -ms /bin/bash myuser

# Switch to the non-root user
USER myuser

# Make port 7860 available to the world outside this container
EXPOSE 7860

# Run app.py when the container launches
CMD ["python", "app.py"]