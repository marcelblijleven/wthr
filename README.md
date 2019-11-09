# wthr
Store darksky weather info in influxdb

## env variables

## docker
Clone the repository and build the docker image
```bash
docker build -t wthr .
```

Copy default.env to .env and fill in the values, then run the image
```bash
docker run --env-file .env wthr
```

## influxdb
Create a db, which keeps the data for 7 days.
```
CREATE DATABASE {db_name} WITH DURATION 7d
```

Grant permissions to the user you want to use
```bash
GRANT ALL ON {db_name} TO {user}
```