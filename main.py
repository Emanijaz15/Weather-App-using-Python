import requests

try:
    user=input("Enter city name to check Weather: ")
    api_key="198dec3434954733a2694735250107"
    weather_response=f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={user}"

    response = requests.get(weather_response)
    data = response.json()
    name=data["location"]["name"]
    region=data["location"]["region"]
    country=data["location"]["country"]
    time=data["location"]["localtime"]
    print(f"Weather of {name},{region},{country} at {time}")
    temp_in_c=data["current"]["temp_c"]
    print(f"Temperature in Celsius: {temp_in_c}")
    condition=data["current"]["condition"]["text"]
    print(f"Condition: {condition}")
    humidity=data["current"]["humidity"]
    print(f"Humidity: {humidity}")
    wind=data["current"]["wind_kph"]
    print(f"Wind (kph): {wind}")
except KeyError:
    print("Error: Could not find expected data in the response.")

