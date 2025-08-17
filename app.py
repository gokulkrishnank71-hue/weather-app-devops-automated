from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "your_openweathermap_api_key"  # 🔑 Replace with your actual API key


@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    error = None
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            data = response.json()

            if data.get("cod") == 200:
                weather = {
                    "city": data["name"],
                    "temperature": data["main"]["temp"],
                    "description": data["weather"][0]["description"],
                    "icon": data["weather"][0]["icon"],
                }
            else:
                error = "City not found. Please try again."

    return render_template("index.html", weather=weather, error=error)


@app.route("/health")
def health():
    return "✅ App is running fine! (Updated 🚀)"  # 🔥 Small change here for test commit


if __name__ == "__main__":
    app.run(debug=True)

