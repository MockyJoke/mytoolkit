
FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y vim nginx openssl tmux nano
# RUN apt-get install -y net-tools
# Configure container to run as an executable
# ENTRYPOINT ["/bin/bash"]
CMD ["nginx", "-g", "daemon off;"]
