from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

WEATHER_API = "bfa4849610107bba34496e2ca3c0acef"
NEWS_API = "afd7c6172a954aab993db08c846ff19d"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/weather", methods=["POST"])
def weather():
    try:
        data = request.json
        lat, lon = data["lat"], data["lon"]

        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_API}&units=metric"
        res = requests.get(url).json()

        return jsonify({
            "city": res["name"],
            "temp": res["main"]["temp"],
            "condition": res["weather"][0]["description"]
        })
    except:
        return jsonify({
            "city": "Dumka",
            "temp": 29,
            "condition": "clear sky"
        })

@app.route("/news")
def news():
    try:
        url = f"https://newsapi.org/v2/top-headlines?country=us&pageSize=6&apiKey={NEWS_API}"
        res = requests.get(url).json()

        if res.get("status") != "ok":
            raise Exception("API failed")

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

        # 🔁 fallback data (ALWAYS WORKS)
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

if __name__ == "__main__":
    app.run(debug=True)