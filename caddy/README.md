```
docker run -d --network host -v $(pwd)/Caddyfile:/etc/Caddyfile -v $(pwd)/secrets:/root/.caddy -e ACME_AGREE=true --restart=always --name=caddy_c abiosoft/caddy
```