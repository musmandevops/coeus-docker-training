# Docker Workflow

This guide outlines the process of taking your application code and deploying it as a containerized application using Docker.

## Workflow Overview

Application code --> Dockerfile --> Docker image --> Docker Compose --> Container


## Commands

### Building Docker Image

To build a Docker image:


docker build -t coeus-app:0.1 .


### Running a Container from the Docker Image
To run a container from the image:

docker run --rm --name coeus-app -p 8080:8080 coeus-app:0.1


### Renaming Docker Image
To tag (rename) your Docker image for Docker Hub:

docker tag coeus-app:0.1 coeusdevops/coeus-app:0.1

### Logging into Docker Hub
To log in to Docker Hub:

docker login

### Pushing Docker Image to Docker Hub
To push the Docker image to Docker Hub:

docker push coeusdevops/coeus-app:0.1

### Running Application Through Docker Compose
To start the application using Docker Compose:

docker compose up

To run in the background, use -d:

docker compose up -d

### Stopping Application Through Docker Compose
To stop the application and remove containers:

docker compose down


### Other Useful Commands

#### Checking Docker Images
List all Docker images:

docker images

### Checking Running Containers

#### List all running containers:


docker ps -a


### Additional Resources
For more commands and detailed information, refer to the https://docs.docker.com/get-started/docker_cheatsheet.pdf.



#### Mysql Queries used during session ####

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    firstname VARCHAR(100),
    lastname VARCHAR(100),
    email VARCHAR(150),
    reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (firstname, lastname, email, reg_date) VALUES ('John', 'Doe', 'john.doe@example.com', NOW());
