# 🇮🇳 BharatSense – Smart Weather & Safety Dashboard

🔗 **Live Demo:** https://bharat-sense.onrender.com/
💻 **GitHub Repo:** https://github.com/sahilhansda/bharatsense-dashboard

---

## 📌 Overview

**BharatSense** is a modern web-based dashboard that provides **real-time weather updates, safety alerts, and global emergency news**.
The project is designed with a clean, responsive UI inspired by modern platforms and deployed on cloud infrastructure.

---

## 🚀 Features

* 🌍 **Auto Location Detection** (Geolocation API)
* 🌤 **Real-Time Weather Data** (Temperature, Conditions)
* ⚠️ **Smart Alerts System** (Heatwave / Cold warnings)
* 📰 **Global Emergency News** (with images & descriptions)
* 🧊 **Modern UI/UX** (Glassmorphism, blur effects, animations)
* 📱 **Responsive Design** (works on mobile & desktop)
* 🔁 **Fallback Data System** (ensures app works even if APIs fail)

---

## 🛠️ Tech Stack

### Frontend

* HTML5
* Tailwind CSS
* JavaScript

### Backend

* Python
* Flask

### APIs Used

* OpenWeatherMap API
* NewsAPI

### Deployment

* Render (Cloud Hosting)
* Git & GitHub (Version Control)

---

## 📁 Project Structure

```
smart_dashboard/
│── app.py
│── requirements.txt
│── Procfile
│── runtime.txt
│── .gitignore
│── templates/
│     └── index.html
│── static/
│     ├── script.js
│     └── assets/
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```
git clone https://github.com/sahilhansda/bharatsense-dashboard.git
cd bharatsense-dashboard
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Setup Environment Variables

Create `.env` file:

```
WEATHER_API=your_openweather_api_key
NEWS_API=your_newsapi_key
```

### 4️⃣ Run Locally

```
python app.py
```

Open:

```
http://127.0.0.1:5000
```

---

## 🌐 Deployment

The project is deployed on **Render** using:

* Gunicorn server
* Environment variables for API security
* Python runtime configuration

---

## 🔐 Security

* API keys are stored using **environment variables**
* `.env` file is excluded via `.gitignore`
* No sensitive data is exposed in source code

---

## 🧠 Learning Outcomes

* Full-stack web development using Flask
* API integration & data handling
* Cloud deployment & environment configuration
* Modern UI/UX design principles
* Version control with Git & GitHub

---

## 🎯 Future Improvements

* 🌍 Interactive map integration (Leaflet.js)
* 📊 Weather analytics & charts
* 🔔 Push notifications for alerts
* 🌗 Dark/Light mode toggle
* 👤 User authentication system

---

## 👨‍💻 Author

**Sahil Hansda**
📍 India

---

## 📜 License

This project is created for educational purposes.
