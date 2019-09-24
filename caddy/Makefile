run:
	docker run -d --network host -v $(shell pwd)/Caddyfile:/etc/Caddyfile -v $(shell pwd)/secrets:/root/.caddy -e ACME_AGREE=true --restart=always --name=caddy_c abiosoft/caddy
