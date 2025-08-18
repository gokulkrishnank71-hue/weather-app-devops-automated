from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)

API_KEY = "a68ff2c3bb4621248bd338437e7edbd3"  # 🔑 Replace this with your actual API key

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    error = None
    if request.method == "POST":
        city = request.form.get("city")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if data.get("cod") != 200:
            error = "City not found. Please try again."
        else:
            weather = {
                "city": data["name"],
                "country": data["sys"]["country"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "icon": data["weather"][0]["icon"],
                "sunrise": datetime.utcfromtimestamp(data["sys"]["sunrise"] + data["timezone"]).strftime('%H:%M:%S'),
                "sunset": datetime.utcfromtimestamp(data["sys"]["sunset"] + data["timezone"]).strftime('%H:%M:%S'),
                "wind": data["wind"]["speed"],
                "humidity": data["main"]["humidity"],
                "pressure": data["main"]["pressure"],
                "flag_url": f"https://flagcdn.com/48x36/{data['sys']['country'].lower()}.png"
            }

    return render_template("index.html", weather=weather, error=error)

if __name__ == "__main__":
    app.run(debug=True)

