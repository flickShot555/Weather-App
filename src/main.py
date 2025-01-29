from weather_api import get_weather

def main():
    city = input("Enter city name: ")
    weather = get_weather(city)
    
    if "error" in weather:
        print(weather["error"])
    else:
        print(f"Weather in {weather['city']}: {weather['weather']}, {weather['temperature']}°C")

if __name__ == "__main__":
    main()
