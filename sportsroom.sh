#!/bin/bash

# check if container is running
DOCKER_RUNNING="$(docker inspect -f '{{.State.Running}}' sportsroom)"
echo "$DOCKER_RUNNING"
if [ DOCKER_RUNNING ]; then
echo "Stopping current instance of SportsRoom..."
docker container stop sportsroom
fi

# cleanup
if [ "$(docker ps -aq -f status=exited -f name=sportsroom)" ]; then
echo "Removing current instance of SportsRoom..."
docker container rm sportsroom
fi

# start a new container instance
echo "Starting SportsRoom using rundeck"
# docker-compose
docker run -d -p 8000:8000 --name sportsroom sportsroom  