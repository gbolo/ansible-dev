# remove all hyperledger peer containers
docker stop $(docker ps -a --format='{{.Names}}' --filter "name=vp*")
docker rm $(docker ps -a --format='{{.Names}}' --filter "name=vp*")
# remove all hyperledger chaincode containers
docker stop $(docker ps -a --format='{{.Names}}' --filter "name=dev-vp*")
docker rm $(docker ps -a --format='{{.Names}}' --filter "name=dev-vp*")
# remove chaincode images
docker rmi $(docker images --format='{{.Repository}}' | grep -i dev-vp)
