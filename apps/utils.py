def safe_assign(obj, prop, to_type, default):
    try:
        return to_type(obj[prop])
    except (KeyError, TypeError):
        return default


def check_daytime(time, daily_data):
    daytime = False
    daytime_show = -1
    nighttime_show = 0

    for day in daily_data:
        sunrise_time = day['sunriseTime']
        sunset_time = day['sunsetTime']

        if sunrise_time < time < sunset_time:
            daytime = True
            daytime_show = 0
            nighttime_show = -1

            return daytime, daytime_show, nighttime_show

    return daytime, daytime_show, nighttime_show


def get_sun_status(daytime, cloud_cover):
    return 1 - cloud_cover if daytime else 0


def forecast_to_points(forecast):
    daily_data = forecast['daily']['data']
    hourly_data = forecast['hourly']['data']
    today = daily_data[0]

    data = []

    for hour in hourly_data:
        daytime, daytime_show, nighttime_show = check_daytime(hour['time'], daily_data)
        cloud_cover = safe_assign(hour, 'cloudCover', float, 0.0)
        sun_status = get_sun_status(daytime, cloud_cover)

        points = [
            {
                'measurement': 'forecast',
                'fields': {
                    'apparent_temperature': safe_assign(hour, 'apparentTemperature', float, 0.0),
                    'temperature': safe_assign(hour, 'temperature', float, 0.0),
                    'cloud_cover': cloud_cover,
                    'sun_status': sun_status,
                    'dew_point': safe_assign(hour, 'dewPoint', float, 0.0),
                    'humidity': safe_assign(hour, 'humidity', float, 0.0),
                    'precip_intensity': safe_assign(hour, 'precipIntensity', float, 0.0),
                    'precip_probability': safe_assign(hour, 'precipProbability', float, 0.0),
                    'pressure': safe_assign(hour, 'pressure', float, 0.0),
                    'uv_index': safe_assign(hour, 'uvIndex', int, 0),
                    'visibility': safe_assign(hour, 'visibility', float, 0.0),
                    'wind_bearing': safe_assign(hour, 'windBearing', float, 0.0),
                    'wind_gust': safe_assign(hour, 'windGust', float, 0.0),
                    'wind_speed': safe_assign(hour, 'windSpeed', float, 0.0),
                    'sunrise': safe_assign(today, 'sunriseTime', int, 0),
                    'sunset': safe_assign(today, 'sunsetTime', int, 0),
                    'daytime_show': daytime_show,
                    'nightime_show': nighttime_show,
                    'moon_phase': safe_assign(today, 'moonPhase', float, 0.0),
                    'ozone': safe_assign(hour, 'ozone', float, 0.0),
                },
                'tags': {
                    'source': 'darksky-api',
                    'app': 'wthr'
                }
            }
        ]

        data.append(points)

    return data
