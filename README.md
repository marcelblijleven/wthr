# wthr
Retrieve weather info from the Darksky api and store it in an influxdb database

## Deprecated
Since the Darksky API will stop in 2021, this project is now deprecated

## env variables
| var              | val                     |
|------------------|-------------------------|
| DARKSKY_KEY      | Darsky api key          |
| DARKSKY_LAT      | latitude                |
| DARKSKY_LONG     | longitude               |
| DARKSKY_LANGUAGE | language, default is nl |
| DARKSKY_UNITS    | units, default is ca    |
| INFLUX_HOST      | influxdb host           |
| INFLUX_PORT      | influxdb port           |
| INFLUX_USER      | influxdb username       |
| INFLUX_PASSWORD  | influxdb password       |
| INFLUX_DB        | influxdb database       |

### docker
Clone the repository and build the docker image
```bash
docker build -t wthr .
```

Copy default.env to .env and fill in the values, then run the image
```bash
docker run --env-file .env wthr
```

### influxdb
Create a db, which keeps the data for 7 days.
```
CREATE DATABASE {db_name} WITH DURATION 7d
```

Grant permissions to the user you want to use
```bash
GRANT ALL ON {db_name} TO {user}
```

#### Acknowledgements
Inspired by Erwin Steffens' [ darksky-influxdb](https://github.com/ErwinSteffens/darksky-influxdb) project
