#!/bin/bash
echo Creating detination directory...
mkdir /ssl
echo Requesting certificate...
/usr/bin/certbot certonly -n --email $2 --domains "$1" --agree-tos --standalone --text
echo Copying server certificate to ssl directory...
cp -L /etc/letsencrypt/live/$1/fullchain.pem /ssl/serverCert.pem
cp -L /etc/letsencrypt/live/$1/privkey.pem /ssl/serverKey.pem
cp -L /etc/letsencrypt/live/$1/chain.pem /ssl/caCert.pem

