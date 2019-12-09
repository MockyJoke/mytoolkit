WORK_DIR=$(PWD)/env

run: init_local
	cd $(WORK_DIR) && \
	docker run -d --network host -v $(WORK_DIR)/config.json:/etc/v2ray/config.json --restart=always --name=v2ray_c v2ray/official

init_local:
	python3 ../../../init_instance_env.py env/opconfig.json

create_env:
	mkdir env -p
	cp opconfig.json env/opconfig.json