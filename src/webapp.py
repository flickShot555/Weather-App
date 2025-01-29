from flask import Flask, request, jsonify, render_template
from weather_api import get_weather_data

app = Flask(__name__,template_folder='templates')

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/weather', methods=['GET'])
def get_weather():
    lat = request.args.get("lat")
    lon = request.args.get("lon")

    if not lat or not lon:
        return jsonify({"error": "Missing latitude or longitude"}), 400

    weather = get_weather_data(lat, lon)
    return jsonify(weather)

if __name__ == "__main__":
    app.run(debug=True)
