import requests

def get_weather_data(lat, lon):
    """Fetch weather data from Open-Meteo API"""
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    
    try:
        response = requests.get(url)
        data = response.json()
        return data["current_weather"]
    except Exception as e:
        return {"error": str(e)}
