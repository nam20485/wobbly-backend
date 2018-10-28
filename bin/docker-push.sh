#! /bin/bash

export REMOTE_DOCKER_PATH="${DOCKER_REPO}"/"${NAMESPACE}"/"${2}"

# tag with branch and travis build number then push
export TAG="$TRAVIS_BUILD_NUMBER"
echo Tagging with "$TAG"
docker tag "$DOCKER_IMAGE" "$REMOTE_DOCKER_PATH":"$TAG"    
docker push "$REMOTE_DOCKER_PATH":"$TAG"

# tag with "latest" then push
echo Tagging with latest
docker tag "$DOCKER_IMAGE" "$REMOTE_DOCKER_PATH"
docker push "$REMOTE_DOCKER_PATH"