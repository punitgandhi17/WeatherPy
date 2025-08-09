# imports the requests library so you can make HTTP requests to web services
import requests
print("⚠️⚠️Enter 'Stop' to exit the program")
while(True):
    city = input("Enter city name: ")

    # wttr.in provides weather info in text format
    url = f"https://wttr.in/{city}?format=\n⬛%C+\n⬛feels like %t+\n⬛humidity:%h"

    try:
        response = requests.get(url)
        if(city=="Stop"):
            exit(0)
        elif response.status_code == 200:
            print("----------------------------------------------")
            print(f"\nWeather in {city.capitalize()}: {response.text}")
            print("----------------------------------------------")
        else:
            print("----------------------------------------------")
            print("⚠️⚠️Error: Could not fetch weather.⚠️⚠️")
            print("----------------------------------------------")
    except requests.exceptions.RequestException:
        print("-------------------------------")
        print("⚠️⚠️Network error.⚠️⚠️️")
        print("-------------------------------")
  
