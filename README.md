# wobbly-backend

## Directions

### Fill in Django secret key

`$  mv bin/environment.sh.example bin/environment.sh`

```sh
#bin/environment.sh:

#! /bin/bash

export DOCKER_IMAGE=wobbly-backend-image
export DJANGO_SECRET_KEY= <Django secret key    # (generate <= 32 characters)>
export DEBUG=True
```

### Make scripts executable

`$ chmod +x ./bin/*.sh`

### Set environment variables (for development only)

`$ source bin/environment.sh`

### Build Docker image

`$ bin/build-docker.sh -d`

### Start Docker image

`$ bin/start-docker.sh -d`

Once it starts up the IP address and port will be displayed. Opening a browser to the address will connect you sto the Django server. 

Ctrl-C can be used to gracefully shutdown the service.

### REST API

When running, the server provides the following URLs:

1. REST API - http://0.0.0.0:8000/
2. Schema - http://0.0.0.0:8000/schema
2. Swagger-ified REST API - http://0.0.0.0:8000/swagger
3. REST API documentation - http://0.0.0.0:8000/docs
4. (account login views) - http://0.0.0.0:8000/account/...