from weather_data import WeatherData

test_dict = {'humidity': 93, 'temp': 37.4, 'rain': {'3h': 4}, 'status': 'light rain', 'wind': 1.5, 'clouds': 90, 'snow': {'3h': 5}}

def test_clothing():
    w = WeatherData()
    w.weather_dict = test_dict
    w.determine_clothing()
    assert w.clothing["boots"] == True
    assert w.clothing["sun hat"] == False


def test_weather_object():
    w = WeatherData()
    w.get_weather()
    assert type(w.weather_dict["humidity"]) == int
    assert type(w.weather_dict["status"]) == str


def test_user_provided_location():
    w = WeatherData("london")
    assert w.userProvidedLocation == True
    w.get_weather()
    assert w.location == "London"
    w2 = WeatherData()
    assert w2.userProvidedLocation == False
