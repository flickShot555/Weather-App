from flask import Flask, request, render_template
from weather_api import get_weather

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    if request.method == "POST":
        city = request.form["city"]
        weather = get_weather(city)
    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)
