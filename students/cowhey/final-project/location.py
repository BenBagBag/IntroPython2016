import urllib.request as ur
import json
import pyowm

openweather_api = "b5158610d2e704cb0db72c02fbdd4bbb"
# docs for open weather api: https://github.com/csparpa/pyowm
# better docs: https://github.com/csparpa/pyowm/wiki/Usage-examples

owm = pyowm.OWM(openweather_api)

def get_location():
    url = "http://freegeoip.net/json/"
    location = json.loads(ur.urlopen(url).read().decode("utf-8"))
    return "{}, {}, {}".format(location["city"], location["region_name"], location["country_code"])


def get_weather(location):
    # weather needs to be in x,y format
    weather_dict = {}
    local_weather = owm.weather_at_place(location)
    current_weather = local_weather.get_weather()
    weather_dict["status"] = current_weather.get_detailed_status()
    weather_dict["rain"] = current_weather.get_rain()
    weather_dict["snow"] = current_weather.get_snow()
    weather_dict["temp"] = current_weather.get_temperature(unit="fahrenheit")["temp"]
    weather_dict["humidity"] = current_weather.get_humidity()
    weather_dict["wind"] = current_weather.get_wind()["speed"]
    weather_dict["clouds"] = current_weather.get_clouds()
    return weather_dict


def determine_clothing(weather_dict):
    clothing = {
        "parka": False,
        "rain coat": False,
        "shorts": False,
        "sweatshirt": False,
        "boots": False,
        "sandals": False,
        "warm hat": False,
        "sun hat": False
    }
    # wear a parka and a hat if it's cold
    if weather_dict["temp"] < 40 or weather_dict["snow"] or "snow" in weather_dict["status"].lower():
        clothing["parka"] = True
        clothing["warm hat"] = True
        clothing["boots"] = True
    # wear a rain coat if it's raining
    if (weather_dict["rain"] or "rain" in weather_dict["status"].lower()) and not clothing["parka"]:
        clothing["rain coat"] = True
        clothing["boots"] = True
    # wear a sweatshirt if it's mild weather
    if 40 <= weather_dict["temp"] <= 65:
        clothing["sweatshirt"] = True
    # wear a hat and shorts if it's less than 40% cloud cover and it's hot
    if not weather_dict["clouds"] > 40 and weather_dict["temp"] > 65:
        clothing["sun hat"] = True
        clothing["sandals"] = True
        clothing["shorts"] = True
    return clothing


# l = get_location()
# w = get_weather(l)
# c = determine_clothing(w)
# print(w)
# print(c)
