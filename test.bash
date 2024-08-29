sudo docker image build . -t python-dev
sudo docker container run --rm -v $(pwd):/app --name python-dev python-dev
