from weather_api import get_weather_data

def main():
    lat = input("Enter latitude: ")
    lon = input("Enter longitude: ")
    weather = get_weather_data(lat, lon)

    if "error" in weather:
        print("Error fetching weather data:", weather["error"])
    else:
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Windspeed: {weather['windspeed']} km/h")

if __name__ == "__main__":
    main()
