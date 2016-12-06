from flask import Flask, render_template
import location
app = Flask(__name__)

@app.route('/')
def hello_world():
    city = location.get_location()
    weather = location.get_weather(city)
    # current_condition = weather.get_detailed_status()
    # feed a dictionary into this
    return render_template("index.html", weather=weather)
