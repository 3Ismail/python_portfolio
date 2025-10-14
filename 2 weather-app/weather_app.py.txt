def get_weather(city):
    weather_data = {
        "casablanca": "☀️ Sunny, 27°C",
        "rabat": "🌤️ Partly Cloudy, 25°C",
        "marrakech": "☀️ Hot, 32°C",
        "fes": "🌧️ Rainy, 20°C"
    }
    return weather_data.get(city.lower(), "City not found. Try again!")

def main():
    print("=== Simple Weather App ===")
    city = input("Enter a city name: ")
    result = get_weather(city)
    print(f"Weather in {city.capitalize()}: {result}")

if __name__ == "__main__":
    main()
