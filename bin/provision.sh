#! /bin/bash

export CLUSTER_NAME="wobbly-backend-cluster"
export DEPLOYMENT_NAME="wobbly-backend-deployment"

# create kubernetes cluster
#gcloud container clusters create $CLUSTER_NAME

# authenticate to new cluster
gcloud container clusters get-credentials $CLUSTER_NAME

# deploy image to cluster
#kubectl run $DEPLOYMENT_NAME --image $REMOTE_DOCKER_PATH --port 8000

kubectl set image "$CLUSTER_NAME"/"$DEPLOYMENT_NAME" "$DEPLOYMENT_NAME"="$REMOTE_DOCKER_PATH":latest

# expose service
kubectl expose deployment $DEPLOYMENT_NAME --type LoadBalancer --port 8000 --target-port 8000