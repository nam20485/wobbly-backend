#! /bin/bash

export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)"

echo "deb https://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

sudo apt-get update -qqy
sudo apt-get install -qqy google-cloud-sdk=219.0.1-0