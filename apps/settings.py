import os


class DarkskySettings:
    key = os.getenv('DARKSKY_KEY')
    lat = os.getenv('DARKSKY_LAT')
    long = os.getenv('DARKSKY_LONG')
    units = os.getenv('DARKSKY_UNITS')
    language = os.getenv('DARKSKY_LANGUAGE')


class InfluxdbSettings:
    host = os.getenv('INFLUX_HOST')
    port = os.getenv('INFLUX_PORT')
    username = os.getenv('INFLUX_USER')
    password = os.getenv('INFLUX_PASSWORD')
    database = os.getenv('INFLUX_DB')
