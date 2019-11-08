def safe_assign(obj, prop, default=None):
    try:
        return obj[prop]
    except (TypeError, KeyError):
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
                    current, 'apparentTemperature'
                ),
                'cloudCover': safe_assign(current, 'cloudCover', 0.0),
                'sun': 1 - safe_assign(current, 'cloudCover', 0.0),
                'dewPoint': safe_assign(current, 'dewPoint'),
                'humidity': safe_assign(current, 'humidity'),
                'icon': safe_assign(current, 'icon'),
                'ozone': safe_assign(current, 'ozone'),
                'precipIntensity': safe_assign(current, 'precipIntensity', 0),
                'precipProbability': safe_assign(
                    current, 'precipProbability', 0
                ),
                'pressure': safe_assign(current, 'pressure'),
                'summary': safe_assign(current, 'summary', ''),
                'temperature': safe_assign(current, 'temperature', 0),
                'time': safe_assign(current, 'time'),
                'uvIndex': safe_assign(current, 'uvIndex', 0),
                'visibility': safe_assign(current, 'visibility', 0),
                'windBearing': safe_assign(current, 'windBearing', 0),
                'windGust': safe_assign(current, 'windGust', 0),
                'windSpeed': safe_assign(current, 'windSpeed', 0),

                # Today weather
                'apparentTemperatureMax': safe_assign(
                    today, 'apparentTemperatureMax'
                ),
                'apparentTemperatureMin': safe_assign(
                    today, 'apparentTemperatureMin'
                ),
                'daySummary': safe_assign(today, 'summary', ''),
                'sunriseTime': safe_assign(today, 'sunriseTime'),
                'sunsetTime': safe_assign(today, 'sunsetTime'),
                'temperatureMax': safe_assign(today, 'temperatureMax'),
                'temperatureMin': safe_assign(today, 'temperatureMin'),
                'temperatureHigh': safe_assign(today, 'temperatureHigh'),
                'temperatureLow': safe_assign(today, 'temperatureLow'),
                'dayWindBearing': safe_assign(today, 'windBearing', 0),
                'dayVisiblity': safe_assign(today, 'visibility', 0),
                'moonPhase': safe_assign(today, 'moonPhase', 0),
                'dayPrecipIntensity': safe_assign(today, 'precipIntensity', 0),
                'dayPrecipProbability': safe_assign(today, 'precipProbability', 0),
                'dayPrecipType': safe_assign(today, 'precipType', '')
            },
            'tags': {
                'source': 'darksky-api'
            }
        }
    ]

    return schema
