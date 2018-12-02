# wobbly-backend

The wobbly-backend is composed of a web application serving a REST API. It is implemented in python, using the Django framework backed by a postgresql database. The service is containerized using Docker. Setting up and running the service on your local machine will result in a complete and self-contained development environment, which be accomplished by following the directions below.

## Requirements

The development environment is currently supported only on Linux systems. Docker is required to be installed, and an IDE such as Visual Studio Code is necessary to modify the source code.

If you don't have access to Linux/are working on a Windows machine, Oracle's Virtual Box can be used to install and run a Linux virtual machine. Mint Linux is recommended.

>Basic programming skills and experience are required to effectively contribute to development in the backend codebase. A general working knowledge of development, and specifically python, Django, and git, are necessary tools to contribute. An IDE is required- most developers on the team use Visual Studio Code, a simple yet powerful IDE, to efficiently edit the source code. **Volunteers lacking in this skillset and key areas of knowledge can still contribute, but will need to complete the ramp-up and training process prior to modifying the production codebase.** Prior to making submissions in the codebase or suggesting fundamental changes, please take the time to understand the architecture that we currently have in place and to discuss the existing design with the current developers. The first place to start is to fill out the new developer questionnaire in the Discourse forum and to have an introduction meeting with the existing members, so we can get to know you. If you plan to develop it will also be important to have a meeting with the developers to understand where you fit in and the design choices we have already made. There are also architecture documents to help familiarize yourself with our system and our product goals.

## Setup

### Install Visual Studio Code

Use your package manager or download and run an installer from Microsoft's website.

### Install Docker

Use your package manager or download and run an installer from the Docker website. Docker CE (Community Edition) version is required and free to use. Other offerings such as Docker Machine are not compatible.

### Fill in Django secret key

Update the `bin/environment.sh.example` script file with a secret key

```sh
#bin/environment.sh:

#! /bin/bash

export DOCKER_IMAGE="wobbly-app-backend-image"
export DOCKER_SERVICE="wobbly-app-backend-service"
export DOCKER_LOGGING="json-file"

export DJANGO_SECRET_KEY="Add Django secret key here"    # (random 32 characters)
```

`$  mv bin/environment.sh.example bin/environment.sh`

### Make scripts executable

`$ chmod +x ./bin/*.sh`

### Set environment variables

`$ source bin/environment.sh`

### Build Docker image

`$ bin/build-docker.sh -d`

### Start Docker image

`$ bin/start-docker.sh -d`

Once it starts up the IP address and port will be displayed. Opening a browser to the address will connect you to the Django server.

Back in the terminal, `Ctrl-C` can be used to gracefully shutdown the service.

## REST API

When running, the server provides the following URLs:

1. REST API - <http://0.0.0.0:8000/>
2. Schema - <http://0.0.0.0:8000/schema>
3. Swagger-ified REST API - <http://0.0.0.0:8000/swagger>
4. REST API documentation - <http://0.0.0.0:8000/docs>
5. (account login views) - <http://0.0.0.0:8000/account/...>