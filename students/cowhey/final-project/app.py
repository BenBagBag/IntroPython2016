from flask import Flask, render_template
from weather_data import WeatherData
app = Flask(__name__)

test_weather = {'humidity': 93, 'temp': 37.4, 'rain': {'3h': 4}, 'status': 'light rain', 'wind': 1.5, 'clouds': 90, 'snow': {'3h': 5}}

@app.route('/')
def hello_world():
    data = WeatherData()
    return render_template("index.html", city=data.location, weather=data.weather_dict, clothing=data.clothing)

@app.route('/faq')
def faq():
    return render_template('faq.html')
