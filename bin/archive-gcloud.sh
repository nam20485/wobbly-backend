#! /bin/bash

export CLOUDSDK_CORE_DISABLE_PROMPTS=1

openssl aes-256-cbc -K $encrypted_b48b32dc2f5c_key -iv $encrypted_b48b32dc2f5c_iv -in credentials.tar.gz.enc -out credentials.tar.gz -d
tar -xzf credentials.tar.gz
mkdir -p lib

gcloud auth activate-service-account --key-file client-secret.json
gcloud config set project wobbly-backend        
gcloud auth print-access-token | docker login -u oauth2accesstoken --password-stdin $DOCKER_REPO

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