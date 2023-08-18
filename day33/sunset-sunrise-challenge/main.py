import requests

IRBID_LONG = 35.847908
IRBID_LAT = 32.556957


def sunset(lng, lat, time_format):
    """
    Get the hour of the sunset time at a given location.

    :param lng: The longitude of the location.
    :type lng: float
    :param lat: The latitude of the location.
    :type lat: float
    :param time_format: The desired time format for the output.
    :type time_format: bool

    :return: The hour of the sunset time in the specified format.
    :rtype: int
    """
    response = requests.get(url="https://api.sunrise-sunset.org/json",
                            params={"lat": lat, "lng": lng, "formatted": time_format})
    data = response.json()
    return int(data["results"]["sunset"].split('T')[1].split(':')[0])


def sunrise(lng, lat, time_format):
    """
    Get the hour of the sunrise time at a given location.

    :param time_format: The desired time format for the output.
    :type time_format: bool
    :param lng: The longitude of the location.
    :type lng: float
    :param lat: The latitude of the location.
    :type lat: float

    :return: The hour of the sunrise time.
    :rtype: int
    """
    response = requests.get(url="https://api.sunrise-sunset.org/json",
                            params={"lat": lat, "lng": lng, "formatted": time_format})
    data = response.json()
    return int(data["results"]["sunrise"].split('T')[1].split(':')[0])
