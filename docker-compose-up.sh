#!/bin/bash
docker compose up -d db
docker compose run --rm rsmanage rsmanage initdb
docker compose up -d

docker exec -u root rs-jobe-1 sh -c "mkdir -p /home/jobe00/.cache /home/jobe00/.config && chmod -R 777 /home/jobe00/.cache /home/jobe00/.config"
docker cp ./figshow rs-jobe-1:/tmp/figshow && \
docker exec -it rs-jobe-1 /usr/bin/python3 -m pip install /tmp/figshow
