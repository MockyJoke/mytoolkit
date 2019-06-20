FROM alpine as builder
ENV ARCH "linux-arm"
ENV VERSION "v4.19.1"

ADD https://github.com/v2ray/v2ray-core/releases/download/${VERSION}/v2ray-${ARCH}.zip v2ray.zip
RUN mkdir /v2ray && cd v2ray && mv ../v2ray.zip . && unzip v2ray.zip

FROM arm32v6/alpine:latest

COPY --from=builder v2ray  /usr/bin/v2ray
ENV PATH /usr/bin/v2ray/:$PATH
EXPOSE 8000
COPY config.json /etc/v2ray/config.json
CMD ["/usr/bin/v2ray/v2ray", "-config=/etc/v2ray/config.json"]
