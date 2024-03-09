# Use the latest Python image from Docker Hub
FROM python:latest

# Set environment variables to ensure Python outputs everything that's printed inside the application rather than buffering it.
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory inside the container
WORKDIR  /app

# Copy the entrypoint file and the project files into the container
COPY ./FlixMovie  /app
ADD ./entrypoint.sh /app

# Change permissions for the entrypoint script to make it executable
RUN chmod +x entrypoint.sh

#  Upgrade pip and install required Python packages
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requierments.txt

# Set the entrypoint command for the container
ENTRYPOINT  ./entrypoint.sh
