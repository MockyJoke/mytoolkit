FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:certbot/certbot && \
    apt-get update && \
    apt-get install -y vim nginx openssl tmux nano certbot net-tools
COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
