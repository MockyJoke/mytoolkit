docker run -d -p 443:443 -p 80:80 -v $(pwd)ssl:/ssl -v $(pwd):/etc/nginx/sites-available mynginx
### Or, run it in a network
docker run -d -p 443:443 -p 80:80 -v $(pwd)/ssl:/ssl -v $(pwd):/etc/nginx/sites-available --net mynet --restart=always mynginx
### Or, run it in host network with name
docker run -d -v $(pwd)/ssl:/ssl -v $(pwd):/etc/nginx/sites-available --net host --restart=always --name=mynginx_c mynginx
