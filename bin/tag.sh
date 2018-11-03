#! /bin/bash

GIT_TAG="$TRAVIS_BRANCH"-"$TRAVIS_BUILD_NUMBER"

git tag -a -m "travis build tag"-"$GIT_TAG"
#git push --tags