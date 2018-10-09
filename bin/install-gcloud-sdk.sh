#! /bin/bash

export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)"

echo "deb https://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
curl -s -S https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

sudo apt-get update -qqy
sudo apt-get install -qqy google-cloud-sdk=219.0.1-0

#export GAE_PYTHONPATH=${HOME}/.cache/google_appengine 
#export PATH=$PATH:${HOME}/google-cloud-sdk/bin 
#export PYTHONPATH=${PYTHONPATH}:${GAE_PYTHONPATH} 
#if [ ! -d "${GAE_PYTHONPATH}" ]; then python scripts/fetch_gae_sdk.py $(dirname "${GAE_PYTHONPATH}"); fi
#if [ ! -d ${HOME}/google-cloud-sdk ]; then curl https://sdk.cloud.google.com | bash; fi        