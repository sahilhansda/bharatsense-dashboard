function getLocation() {
    navigator.geolocation.getCurrentPosition(success, fallback);
}

function success(pos) {
    const lat = pos.coords.latitude;
    const lon = pos.coords.longitude;

    fetch("/weather", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({lat, lon})
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("weather").innerHTML =
            `<h3>${data.city}</h3>
             <p>${data.temp}°C - ${data.condition}</p>`;

        let icon = "https://cdn-icons-png.flaticon.com/512/869/869869.png";

        if (data.condition.includes("rain"))
            icon = "https://cdn-icons-png.flaticon.com/512/414/414974.png";

        document.getElementById("icon").src = icon;
    });

    fetch("/news")
    .then(res => res.json())
    .then(news => {
        let html = "";
        news.forEach(n => {
            html += `
            <div class="bg-white/10 p-4 rounded-xl hover:scale-105 transition">
                <img src="${n.img || 'https://via.placeholder.com/400'}" class="rounded-lg mb-3"/>
                <h3 class="font-bold">${n.title}</h3>
                <p class="text-sm opacity-70">${n.desc || ''}</p>
                <a href="${n.url}" target="_blank" class="text-cyan-400">Read more →</a>
            </div>`;
        });
        document.getElementById("news").innerHTML = html;
    });
}

function fallback() {
    document.getElementById("weather").innerHTML =
        "<p>Using default location (Dumka)</p>";
}