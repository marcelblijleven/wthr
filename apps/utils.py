def safe_assign(obj, prop, to_type, default):
    try:
        return to_type(obj[prop])
    except (KeyError, TypeError):
        return default


def forecast_to_points(forecast):
    current = forecast['currently']
    today = forecast['daily']['data'][0]

    schema = [
        {
            'measurement': 'weather',
            'fields': {
                # Current weather
                'apparentTemperature':  safe_assign(
                    current, 'apparentTemperature', float, 0.0
                ),
                'cloudCover': safe_assign(current, 'cloudCover', float, 0.0),
                'sun': 1 - safe_assign(current, 'cloudCover', float, 0.0),
                'dewPoint': safe_assign(current, 'dewPoint', float, 0.0),
                'humidity': safe_assign(current, 'humidity', float, 0.0),
                'icon': safe_assign(current, 'icon', str, ''),
                'ozone': safe_assign(current, 'ozone', float, 0.0),
                'precipIntensity': safe_assign(current, 'precipIntensity', float, 0.0),
                'precipProbability': safe_assign(
                    current, 'precipProbability', float, 0.0
                ),
                'pressure': safe_assign(current, 'pressure', float, 0.0),
                'summary': safe_assign(current, 'summary', str, ''),
                'temperature': safe_assign(current, 'temperature', float, 0.0),
                'uvIndex': safe_assign(current, 'uvIndex', int, 0),
                'visibility': safe_assign(current, 'visibility', int, 0),
                'windBearing': safe_assign(current, 'windBearing', int, 0),
                'windGust': safe_assign(current, 'windGust', float, 0.0),
                'windSpeed': safe_assign(current, 'windSpeed', float, 0.0),

                # Today weather
                'apparentTemperatureMax': safe_assign(
                    today, 'apparentTemperatureMax', float, 0.0
                ),
                'apparentTemperatureMin': safe_assign(
                    today, 'apparentTemperatureMin', float, 0.0
                ),
                'daySummary': safe_assign(today, 'summary', str, ''),
                'sunriseTime': safe_assign(today, 'sunriseTime', int, 0),
                'sunsetTime': safe_assign(today, 'sunsetTime', int, 0),
                'temperatureMax': safe_assign(today, 'temperatureMax', float, 0.0),
                'temperatureMin': safe_assign(today, 'temperatureMin', float, 0.0),
                'temperatureHigh': safe_assign(today, 'temperatureHigh', float, 0.0),
                'temperatureLow': safe_assign(today, 'temperatureLow', float, 0.0),
                'dayWindBearing': safe_assign(today, 'windBearing', int, 0),
                'dayVisiblity': safe_assign(today, 'visibility', int, 0),
                'moonPhase': safe_assign(today, 'moonPhase', float, 0.0),
                'dayPrecipIntensity': safe_assign(today, 'precipIntensity', float, 0.0),
                'dayPrecipProbability': safe_assign(today, 'precipProbability', float, 0.0),
                'dayPrecipType': safe_assign(today, 'precipType', str, '')
            },
            'tags': {
                'source': 'darksky-api'
            }
        }
    ]

    return schema
