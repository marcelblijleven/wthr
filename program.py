import os

from apps.utils import forecast_to_points
from apps.darksky.client import Darksky
from apps.influxdb.client import Influx
from apps.settings import DarkskySettings, InfluxdbSettings


def program():
    darksky = Darksky(DarkskySettings.key)

    influx = Influx(
        host=InfluxdbSettings.host,
        port=InfluxdbSettings.port,
        username=InfluxdbSettings.username,
        password=InfluxdbSettings.password,
        database=InfluxdbSettings.database
    )

    forecast = darksky.forecast(
        lat=DarkskySettings.lat,
        long=DarkskySettings.long,
        units=DarkskySettings.units,
        language=DarkskySettings.language
    )

    data_points = forecast_to_points(forecast)

    for points in data_points:
        influx.write_points(points)


if __name__ == '__main__':
    program()
