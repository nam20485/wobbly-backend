#! /bin/bash

export CLUSTER_NAME="wobbly-backend-cluster"
export DEPLOYMENT_NAME="wobbly-backend-app"
export COMPUTE_ZONE="us-west2-a"

gcloud config set compute/zone $COMPUTE_ZONE --verbosity="info"

# create kubernetes cluster
#gcloud container clusters create $CLUSTER_NAME

# authenticate to new cluster
gcloud container clusters get-credentials $CLUSTER_NAME --verbosity="info"

# deploy image to cluster
#kubectl run $DEPLOYMENT_NAME --image $REMOTE_DOCKER_PATH --port 8000

# update cluster's deployed image
kubectl set image deployment/"$DEPLOYMENT_NAME" "$DOCKER_IMAGE"="$REMOTE_DOCKER_PATH":latest --v=4

# expose service
kubectl expose deployment $DEPLOYMENT_NAME --type LoadBalancer --port 8000 --target-port 8000 --v=4