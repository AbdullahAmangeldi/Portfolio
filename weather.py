import requests
import json

def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    weather_data = json.loads(response.text)
    
    if weather_data["cod"] == 200:
        temperature = weather_data["main"]["temp"]
        description = weather_data["weather"][0]["description"]
        print(f"Погода в {location}:")
        print(f"Температура: {temperature}°C")
        print(f"Описание: {description}")
    else:
        print("Ошибка в получении информации.")

def main():
    api_key = "9282a5768304477d8a3ac407d7b9936c"  
    location = input("Введите место:")
    get_weather(api_key, location)

if __name__ == "__main__":
    main()
