build:
	docker build -t bootstrap .

init-multiarch:
	docker run --privileged --rm tonistiigi/binfmt --install all
	docker buildx create --name mybuilder
	docker buildx use mybuilder

push:
	docker buildx build --platform linux/amd64,linux/arm64,linux/arm/v7 -t johnsonpan333/bootstrap:latest --push .