# wthr
Store darksky weather info in influxdb for grafana

# docker
Clone the repository and build the docker image
```bash
docker build -t wthr .
```

Copy default.env to .env and fill in the values, then run the image
```bash
docker run --env-file .env wthr
```
