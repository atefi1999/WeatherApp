from flask import Flask, render_template_string, request
import requests

# ------------------- Class 1: WeatherFetcher -------------------
class WeatherFetcher:
    def __init__(self, api_key, base_url="http://api.openweathermap.org/data/2.5/weather"):
        self.api_key = api_key
        self.base_url = base_url

    def get_weather(self, city):
        params = {"q": city, "appid": self.api_key, "units": "metric"}
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()
        return None


# ------------------- Class 2: WeatherData -------------------
class WeatherData:
    def __init__(self, city, temperature, description, humidity, wind_speed):
        self.city = city
        self.temperature = temperature
        self.description = description
        self.humidity = humidity
        self.wind_speed = wind_speed

    def __str__(self):
        return f"{self.city}: {self.temperature}°C, {self.description}, Humidity: {self.humidity}%, Wind: {self.wind_speed} m/s"


# ------------------- Class 3: WeatherManager -------------------
class WeatherManager:
    def __init__(self, fetcher: WeatherFetcher):
        self.fetcher = fetcher

    def get_city_weather(self, city):
        data = self.fetcher.get_weather(city)
        if data:
            return WeatherData(
                city=data["name"],
                temperature=data["main"]["temp"],
                description=data["weather"][0]["description"].title(),
                humidity=data["main"]["humidity"],
                wind_speed=data["wind"]["speed"]
            )
        return None


# ------------------- Class 4: WeatherApp (Web Layer) -------------------
app = Flask(__name__)

# ⚠️ Put your API key here
API_KEY = "YOUR_API_KEY"
weather_manager = WeatherManager(WeatherFetcher(API_KEY))

# Simple template with Jinja2
HTML_TEMPLATE = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Weather App</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 40px; background: #f0f8ff; }
    .container { max-width: 500px; margin: auto; padding: 20px; background: #fff; border-radius: 10px; box-shadow: 0 0 10px #ccc; }
    input, button { padding: 10px; margin-top: 10px; width: 100%; }
    .result { margin-top: 20px; padding: 15px; background: #e6f7ff; border-left: 5px solid #0099cc; }
  </style>
</head>
<body>
  <div class="container">
    <h1>🌤 Weather App</h1>
    <form method="post">
      <input type="text" name="city" placeholder="Enter city name" required>
      <button type="submit">Get Weather</button>
    </form>

    {% if weather %}
      <div class="result">
        <h2>{{ weather.city }}</h2>
        <p><b>Temperature:</b> {{ weather.temperature }} °C</p>
        <p><b>Description:</b> {{ weather.description }}</p>
        <p><b>Humidity:</b> {{ weather.humidity }}%</p>
        <p><b>Wind Speed:</b> {{ weather.wind_speed }} m/s</p>
      </div>
    {% elif error %}
      <div class="result" style="background:#ffe6e6; border-left:5px solid red;">
        <p>{{ error }}</p>
      </div>
    {% endif %}
  </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    error = None
    if request.method == "POST":
        city = request.form.get("city")
        weather = weather_manager.get_city_weather(city)
        if not weather:
            error = "City not found or API error."
    return render_template_string(HTML_TEMPLATE, weather=weather, error=error)


if __name__ == "__main__":
    app.run(debug=True)
