#! /bin/bash

# Tag, Push and Deploy only if it's not a pull request
if [ -z "$TRAVIS_PULL_REQUEST" ] || [ "$TRAVIS_PULL_REQUEST" == "false" ]; then

    # Push only if we're testing the master branch
    #if [ "$TRAVIS_BRANCH" == "master" ]; then

        IMAGE_NAME="${DOCKER_IMAGE}"-"{$TRAVIS_BRANCH}"
        CLUSTER_NAME="wobbly-backend-cluster"-${TRAVIS_BRANCH}
        
        source bin/install-tools.sh
        source bin/authenticate-gcloud.sh
        source bin/docker-push.sh ${IMAGE_NAME}
        source bin/provision.sh ${IMAGE_NAME} ${CLUSTER_NAME}

   #else
    #    echo "Skipping deploy because branch is not master"
    #fi
else
    echo "Skipping deploy because it's a pull request"
fi