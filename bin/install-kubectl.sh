#! /bin/bash

export KUBECTL_REPO="kubernetes-$(lsb_release -c -s)"

sudo apt-get update
sudo apt-get install -y apt-transport-https

curl -s -S https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
echo "deb https://apt.kubernetes.io/ $KUBECTL_REPO main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list

sudo apt-get update -qqy
sudo apt-get install -qqy kubectl