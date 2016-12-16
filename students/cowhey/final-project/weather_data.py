import urllib.request as ur
import json
import pyowm

openweather_api = "b5158610d2e704cb0db72c02fbdd4bbb"
# docs for open weather api: https://github.com/csparpa/pyowm
# better docs: https://github.com/csparpa/pyowm/wiki/Usage-examples

owm = pyowm.OWM(openweather_api)

class WeatherData:
    def __init__(self, location=""):
        # add API key here
        self.openweather_api = SECRET_KEY
        self.clothing = { "parka": False,
                         "rain coat": False,
                         "shorts": False,
                         "sweatshirt": False,
                         "boots": False,
                         "sandals": False,
                         "warm hat": False,
                         "sun hat": False }
        self.weather_dict = {}
        if location:
            self.location = location
            self.userProvidedLocation = True
        else:
            self.location = self.get_location()
            self.userProvidedLocation = False
        self.get_weather()
        # but now they're not printing all clothes
        self.determine_clothing()

    def get_location(self):
        url = "http://freegeoip.net/json/"
        location = json.loads(ur.urlopen(url).read().decode("utf-8"))
        return "{}, {}, {}".format(location["city"], location["region_name"], location["country_code"])

    def get_weather(self):
        local_weather = owm.weather_at_place(self.location)
        if self.userProvidedLocation:
            self.location = local_weather.get_location().get_name()
        current_weather = local_weather.get_weather()
        self.weather_dict["status"] = current_weather.get_detailed_status()
        self.weather_dict["rain"] = current_weather.get_rain()
        self.weather_dict["snow"] = current_weather.get_snow()
        self.weather_dict["temp"] = current_weather.get_temperature(unit="fahrenheit")["temp"]
        self.weather_dict["humidity"] = current_weather.get_humidity()
        self.weather_dict["wind"] = current_weather.get_wind()["speed"]
        self.weather_dict["clouds"] = current_weather.get_clouds()

    def determine_clothing(self):
        # wear a parka and a hat if it's cold
        if self.weather_dict["temp"] < 40 or self.weather_dict["snow"] or "snow" in self.weather_dict["status"].lower():
            self.clothing["parka"] = True
            self.clothing["warm hat"] = True
            self.clothing["boots"] = True
        # wear a rain coat if it's raining and you're not already wearing a parka
        if (self.weather_dict["rain"] or "rain" in self.weather_dict["status"].lower()) and not self.clothing["parka"]:
            self.clothing["rain coat"] = True
            self.clothing["boots"] = True
        # wear a sweatshirt if it's mild weather
        if 40 <= self.weather_dict["temp"] <= 65:
            self.clothing["sweatshirt"] = True
        # wear a hat and shorts if it's less than 40% cloud cover and it's hot
        if not self.weather_dict["clouds"] > 40 and self.weather_dict["temp"] > 65:
            self.clothing["sun hat"] = True
            self.clothing["sandals"] = True
            self.clothing["shorts"] = True
