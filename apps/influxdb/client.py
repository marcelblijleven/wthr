class Influx:
    def __init__(self, host, port, username, password, database):
        from influxdb import InfluxDBClient

        self.client = InfluxDBClient(
            host=host,
            port=port,
            username=username,
            password=password,
            database=database,
        )

    def write_points(self, points):
        self.client.write_points(points,)
        x = self.client.create_retention_policy()
