# 🌤 Weather App (Flask + OpenWeatherMap)

#### A small web app built with Flask that lets users enter a city name and receive current weather information (temperature, description, humidity, wind speed) from the OpenWeatherMap API.


---

## ✨ Features

- Enter any city name and get real-time weather data.
- Temperature displayed in Celsius.
- Shows weather description, humidity, and wind speed.
- Clean, responsive single-page UI (HTML + CSS).
- Simple, easy-to-read code

---

## 🛠 Installation / Run

### 1. Clone the repository

```bash
git clone https://github.com/atefi1999/WeatherApp.git

cd WeatherApp
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt

pip install flask requests
```

### 4. Provide your OpenWeatherMap API key
#### edit weather_app.py:

```bash
API_KEY = "API_KEY"
```

### 5. Run the app

```bash
python weather_app.py
```

### 6. Open in browser

```backtick
Visit: http://127.0.0.1:5000 and enter a city name.
```

---

## ▶️ Example Usage

### Example result shown on page:

```backtick
Tehran
Temperature: 28 °C
Description: Clear Sky
Humidity: 40%
Wind Speed: 3.5 m/s
```

### If the API fails or city is not found, the app shows:

```backtick
City not found or API error.
```

---

## 📂 Project Structure

```markdown
WeatherApp/
├── weather_app.py      # Main Flask application
├── README.md           # This file
└── screenshot.png      # demo screenshot to show in README
```

---

## 🧰 Technologies Used

- Python 3.x
- Flask (web framework)
- requests (HTTP client)
- OpenWeatherMap API (weather data)

---

## ⚠️ Notes & Tips

- Get an API key from OpenWeatherMap (free plan available) and set it as described.
- Do not commit your real API key into a public repository — use environment variables or a .env file (and add .env to .gitignore).
- The app uses units=metric so temperature is Celsius. To use Fahrenheit, change units to imperial.
