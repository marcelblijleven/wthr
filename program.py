import os

from apps.utils import forecast_to_points
from apps.darksky.client import Darksky
from apps.influxdb.client import Influx


def program():
    key = os.getenv('DARKSKY_KEY')
    lat = os.getenv('DARKSKY_LAT')
    long = os.getenv('DARKSKY_LONG')
    units = os.getenv('DARKSKY_UNITS')
    language = os.getenv('DARKSKY_LANGUAGE')

    darksky = Darksky(key)
    influx = Influx(
        host=os.getenv('INFLUX_HOST'),
        port=os.getenv('INFLUX_PORT'),
        username=os.getenv('INFLUX_USER'),
        password=os.getenv('INFLUX_PASSWORD'),
        database=os.getenv('INFLUX_DB')
    )

    forecast = darksky.forecast(lat, long, units=units, language=language)
    data_points = forecast_to_points(forecast)
    influx.write_points(data_points)


if __name__ == '__main__':
    program()
