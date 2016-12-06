from flask import Flask, render_template
import location
app = Flask(__name__)

test_weather = {'humidity': 93, 'temp': 37.4, 'rain': {'3h': 4}, 'status': 'light rain', 'wind': 1.5, 'clouds': 90, 'snow': {'3h': 5}}

@app.route('/')
def hello_world():
    city = location.get_location()
    weather = location.get_weather(city)
    clothing = location.determine_clothing(weather)
    # feed a dictionary into this
    return render_template("index.html", city=city, weather=weather, clothing=clothing)

@app.route('/faq')
def faq():
    return render_template('faq.html')
