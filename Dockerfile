FROM ubuntu:latest
LABEL authors="dpkarasev"

ENTRYPOINT ["top", "-b"]