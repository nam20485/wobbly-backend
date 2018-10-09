#! /bin/bash

export REMOTE_DOCKER_PATH="$DOCKER_REPO"/"$DOCKER_REPO_NAMESPACE"/"$DOCKER_IMAGE"

# tag with branch and travis build number then push
TAG=travis-buildnum-"$TRAVIS_BUILD_NUMBER"
echo Tagging with "$TAG"
docker tag "$DOCKER_IMAGE" "$REMOTE_DOCKER_PATH":"$TAG"    
docker push "$REMOTE_DOCKER_PATH":"$TAG"

# tag with "latest" then push
TAG=latest
echo Tagging with "$TAG"
docker tag "$DOCKER_IMAGE" "$REMOTE_DOCKER_PATH":"$TAG"
docker push "$REMOTE_DOCKER_PATH":"$TAG"