IMAGE_TAG=your-image
CONTAINER_NAME=your-container
WORKDIR=/app

sudo docker image build -t $IMAGE_TAG . > build.log 2>&1
sudo docker container run --name $CONTAINER_NAME $IMAGE_TAG
