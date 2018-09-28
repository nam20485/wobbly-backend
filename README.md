# wobbly-backend

## Directions

### Fill in Django secret key

Update the `bin/environment.sh.example` script file with a secret key

```sh
#bin/environment.sh:

#! /bin/bash

export DOCKER_IMAGE=wobbly-backend-image
export DJANGO_SECRET_KEY= <Add Django secret key here    # (generate <= 32 characters)>
export DEBUG=True
```

`$  mv bin/environment.sh.example bin/environment.sh`

### Make scripts executable

`$ chmod +x ./bin/*.sh`

### Set environment variables (for development only)

`$ source bin/environment.sh`

### Build Docker image

`$ bin/build-docker.sh -d`

### Start Docker image

`$ bin/start-docker.sh -d`

=======
Once it starts up the IP address and port will be displayed. Opening a browser to the address will connect you to the Django server.

Ctrl-C can be used to gracefully shutdown the service.

### REST API

When running, the server provides the following URLs:

1. REST API - http://0.0.0.0:8000/
2. Schema - http://0.0.0.0:8000/schema
3. Swagger-ified REST API - http://0.0.0.0:8000/swagger
4. REST API documentation - http://0.0.0.0:8000/docs
5. (account login views) - http://0.0.0.0:8000/account/...