
IMAGE_TAG=nextjs-image
CONTAINER_NAME=nextjs-container
WORKDIR=/app

sudo docker image build -t $IMAGE_TAG . > build.log 2>&1

sudo docker container run -d --name $CONTAINER_NAME $IMAGE_TAG  
sudo docker container stop $CONTAINER_NAME
sudo docker container cp $CONTAINER_NAME:$WORKDIR/. .
sudo docker container rm $CONTAINER_NAME
sudo chown -R $(whoami):$(whoami) .

sudo docker container run --name $CONTAINER_NAME -p 3000:3000 -v $(pwd):$WORKDIR $IMAGE_TAG
