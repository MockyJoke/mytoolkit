WORK_DIR=$(PWD)/env

run:
	cd $(WORK_DIR) && \
	docker run -d --network host -v $(WORK_DIR)/config.json:/etc/v2ray/config.json --restart=always --name=v2ray_rev_portal v2ray/official

config: build create_env download_opconfig parse_opconfig

build:
	echo "No-op for build"

stop:
	docker rm -f v2ray_rev_portal

# helpers
parse_opconfig:
	python3 ../../../init_instance_env.py env/opconfig.json

download_opconfig:
	curl -v -o env/opconfig.json https://${HITMAN_SERVICE_ENDPOINT}/api/store/settings~v2ray~rev_portal~${HITMAN_HOST_ID}/opconfig.json?key=${HITMAN_HOST_KEY}

upload_opconfig:
	curl -v -X POST -T env/opconfig.json https://${HITMAN_SERVICE_ENDPOINT}/api/store/settings~v2ray~rev_portal~${HITMAN_HOST_ID}/opconfig.json?key=${HITMAN_HOST_KEY}

create_env:
	mkdir env -p
	cp opconfig.json env/opconfig.json