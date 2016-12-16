from flask import Flask, render_template, request, url_for
from weather_data import WeatherData

app = Flask(__name__)


@app.route('/')
def hello_world():
    data = WeatherData()
    return render_template("index.html", city=data.location, weather=data.weather_dict, clothing=data.clothing, searchCity=data.userProvidedLocation)


@app.route('/faq')
def faq():
    return render_template('faq.html', faq=True)


@app.route('/search')
def search():
    return render_template('search.html', searchCity=True)


@app.route('/search', methods=['POST'])
def searchcity():
    city = request.form['city']
    data = WeatherData(city)
    return render_template("index.html", city=data.location, weather=data.weather_dict, clothing=data.clothing, searchCity=data.userProvidedLocation)
