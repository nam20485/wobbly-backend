#! /bin/bash

# Tag, Push and Deploy only if it's not a pull request
if [ -z "$TRAVIS_PULL_REQUEST" ] || [ "$TRAVIS_PULL_REQUEST" == "false" ]; then

    # Push only if we're testing the master branch
    #if [ "$TRAVIS_BRANCH" == "master" ]; then        
        
        TAG=travis-buildnum-"$TRAVIS_BUILD_NUMBER"
        REMOTE_DOCKER_PATH="$DOCKER_REPO"/"$DOCKER_REPO_NAMESPACE"/web

        echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin $DOCKER_REPO        
        docker tag $DOCKER_IMAGE $REMOTE_DOCKER_PATH
        docker push $REMOTE_DOCKER_PATH

        # tag with branch and travis build number then push        
        # echo Tagging with "$TAG"
        # docker tag "$DOCKER_IMAGE":latest "$REMOTE_DOCKER_PATH":"$TAG"    
        # docker push "$REMOTE_DOCKER_PATH":"$TAG"

        # # tag with "latest" then push
        # TAG=latest
        # echo Tagging with "$TAG"
        # docker tag "$DOCKER_IMAGE":latest "$REMOTE_DOCKER_PATH":"$TAG"
        # docker push "$REMOTE_DOCKER_PATH":"$TAG"
    
    #else
    #    echo "Skipping deploy because branch is not master"
    #fi
else
    echo "Skipping deploy because it's a pull request"
fi