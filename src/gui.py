import tkinter as tk
from weather_api import get_weather

def fetch_weather():
    city = city_entry.get()
    weather = get_weather(city)
    
    if "error" in weather:
        result_label.config(text=weather["error"])
    else:
        result_label.config(text=f"{weather['city']}: {weather['weather']}, {weather['temperature']}°C")

# GUI setup
root = tk.Tk()
root.title("Weather App")

city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=10)

fetch_button = tk.Button(root, text="Get Weather", command=fetch_weather)
fetch_button.pack()

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
