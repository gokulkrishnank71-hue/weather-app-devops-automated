from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "a68ff2c3bb4621248bd338437e7edbd3"  # 🔑 Replace with your real API key

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    error = None
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                weather = {
                    "city": data["name"],
                    "temperature": data["main"]["temp"],
                    "description": data["weather"][0]["description"],
                }
            else:
                error = "City not found."
        else:
            error = "Please enter a city name."
    return render_template("index.html", weather=weather, error=error)

@app.route("/health")
def health():
    return {"status": "ok", "message": "App is running!"}

if __name__ == "__main__":
    app.run(debug=True)
