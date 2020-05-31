FROM raspbian/stretch:latest 

RUN apt-get update && \
    apt-get install -y vim tmux less nano net-tools deluged deluge-webui && \
    /usr/bin/deluged

ENTRYPOINT ["/usr/bin/deluge-web"]
