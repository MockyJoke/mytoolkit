#!/bin/bash
# ./request_cert.sh <DOMAIN> <EMAIL>
DOMAIN=$1
EMAIL=$2

sudo apt-get install -y software-properties-common
sudo add-apt-repository -y ppa:certbot/certbot
sudo apt-get update
sudo apt-get install -y certbot
sudo certbot certonly -n --email $EMAIL --domains "$DOMAIN" --agree-tos --standalone --text

mkdir ssl
echo Copying server certificate to ssl directory...
sudo cp -L /etc/letsencrypt/live/$DOMAIN/fullchain.pem ssl/serverCert.pem
sudo cp -L /etc/letsencrypt/live/$DOMAIN/privkey.pem ssl/serverKey.pem
sudo cp -L /etc/letsencrypt/live/$DOMAIN/chain.pem ssl/caCert.pem
echo Done!
