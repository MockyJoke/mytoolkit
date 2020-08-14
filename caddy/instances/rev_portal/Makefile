WORK_DIR=$(PWD)/env

run:
	cd $(WORK_DIR) && \
	docker run -d --network host -v $(WORK_DIR)/Caddyfile:/etc/Caddyfile -v $(WORK_DIR)/secrets:/root/.caddy -e ACME_AGREE=true --restart=always --name=caddy_rev_portal abiosoft/caddy

config: build create_env download_opconfig parse_opconfig

build:
	echo "No-op for build"

stop:
	docker rm -f caddy_rev_portal

# helpers
parse_opconfig:
	python3 ../../../init_instance_env.py env/opconfig.json

download_opconfig:
	curl -v -o env/opconfig.json https://${HITMAN_SERVICE_ENDPOINT}/api/store/settings~caddy~rev_portal~${HITMAN_HOST_ID}/opconfig.json?key=${HITMAN_HOST_KEY}

upload_opconfig:
	curl -v -X POST -T env/opconfig.json https://${HITMAN_SERVICE_ENDPOINT}/api/store/settings~caddy~rev_portal~${HITMAN_HOST_ID}/opconfig.json?key=${HITMAN_HOST_KEY}

create_env:
	mkdir env -p
	cp opconfig.json env/opconfig.json