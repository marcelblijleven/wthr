import requests


class Darksky:
    def __init__(self, key):
        if key is None:
            raise ValueError('Darksky key cannot be None')

        self.key = key

    def forecast(self, lat, long, units='ca', language='nl'):
        url = f'https://api.darksky.net/forecast/{self.key}/{lat},{long}'
        params = {
            'units': units,
            'language': language,
            'exclude': 'minutely,hourly,alerts'
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
        except requests.HTTPError as e:
            raise e

        return response.json()
