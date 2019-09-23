```
docker run -d --network host -v $(pwd)/Caddyfile:/etc/Caddyfile -v $(pwd)/secrets:/root/.caddy -e ACME_AGREE=true --restart=always --name=caddy_c abiosoft/caddy
```

#### Steps to convert Caddy to LetsEncrypt:

* Copy ~/.caddy/acme/acme-v01.api.letsencrypt.org/sites/{yourdomain}/{yourdomain}.crt to **cert.pem**

* Copy the Active 'Intermediate Certificate' from https://letsencrypt.org/certificates/ and safe it as **chain.pem**

* copy cert.pem + chain.pem in that order to one file called **fullchain.pem**

* copy ~/.caddy/acme/acme-v01.api.letsencrypt.org/sites/{yourdomain}/{yourdomain}.key to **privkey.pem**
