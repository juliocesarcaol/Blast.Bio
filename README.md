# crear imagen de servidor blast
cd server
docker rm blastservice
docker build . -t test51 --platform linux/amd64
docker run --name blastservice --network network1 -p 5001:5000 test51

# Para detener 

docker stop blastservice

# Para levantar 

docker start blastservice
