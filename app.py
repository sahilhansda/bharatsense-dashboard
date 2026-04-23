from flask import Flask, render_template, jsonify, request
import requests
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

app = Flask(__name__)

# Secure API keys
WEATHER_API = os.getenv("WEATHER_API")
NEWS_API = os.getenv("NEWS_API")

@app.route("/")
def home():
    return render_template("index.html")

# 🌤 Weather Route
@app.route("/weather", methods=["POST"])
def weather():
    try:
        data = request.json
        lat = data.get("lat")
        lon = data.get("lon")

        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_API}&units=metric"
        res = requests.get(url).json()

        if "main" not in res:
            raise Exception("Weather API failed")

        return jsonify({
            "city": res["name"],
            "temp": res["main"]["temp"],
            "condition": res["weather"][0]["description"]
        })

    except Exception as e:
        print("WEATHER ERROR:", e)
        return jsonify({
            "city": "Dumka",
            "temp": 29,
            "condition": "clear sky"
        })

# 📰 News Route
@app.route("/news")
def news():
    try:
        url = f"https://newsapi.org/v2/top-headlines?country=us&pageSize=6&apiKey={NEWS_API}"
        res = requests.get(url).json()

        if res.get("status") != "ok":
            raise Exception("News API failed")

        articles = []
        for a in res.get("articles", []):
            articles.append({
                "title": a.get("title", "No title"),
                "desc": a.get("description", "No description"),
                "img": a.get("urlToImage") or "https://via.placeholder.com/400",
                "url": a.get("url", "#")
            })

        return jsonify(articles)

    except Exception as e:
        print("NEWS ERROR:", e)
        return jsonify([
            {
                "title": "Heatwave Alert in India",
                "desc": "Temperatures rising across multiple states.",
                "img": "https://via.placeholder.com/400",
                "url": "#"
            },
            {
                "title": "Flood Warning Issued",
                "desc": "Heavy rainfall in eastern regions.",
                "img": "https://via.placeholder.com/400",
                "url": "#"
            }
        ])

# 🚀 Run App (for Render deployment)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))