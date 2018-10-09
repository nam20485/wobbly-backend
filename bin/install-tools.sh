#! /bin/bash

export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)"
export KUBECTL_REPO="kubernetes-$(lsb_release -c -s)"

curl -s -S https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
echo "deb https://apt.kubernetes.io/ $KUBECTL_REPO main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list

echo "deb https://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
curl -s -S https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

sudo apt-get update -qqy && sudo apt-get install -qqy --no-install-recommends apt-transport-https google-cloud-sdk=219.0.1-0 kubectl=1.12.1.-00

