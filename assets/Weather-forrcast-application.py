import requests
from datetime import datetime, timezone

def get_weather(city):
    api_key=#paste your api key within double qoutes without space
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 200:
            data = response.json()

            
            timestamp = data["dt"] + data["timezone"]
            local_time = datetime.fromtimestamp(timestamp, tz=timezone.utc)

            print("\n📍 Weather Report (Website Match)")
            print("----------------------------------")
            print(f"City               : {data['name']}")
            print(f"🌡 Temperature      : {data['main']['temp']} °C")
            print(f"🤔 Feels Like       : {data['main']['feels_like']} °C")
            print(f"💧 Humidity         : {data['main']['humidity']} %")
            print(f"☁ Condition        : {data['weather'][0]['description'].capitalize()}")
            print(f"💨 Wind Speed       : {data['wind']['speed']} m/s")
            print(f"🕒 Data Time        : {local_time.strftime('%d-%m-%Y %I:%M %p')}")

        elif response.status_code == 401:
            print("❌ Invalid API key")

        elif response.status_code == 404:
            print("❌ City not found")

        else:
            print("❌ Error fetching data")

    except requests.exceptions.ConnectionError:
        print("❌ No internet connection")
    except Exception as e:
        print("❌ Error:", e)

while True:
	city_name = input("\nEnter city name: ")
	get_weather(city_name)
	next_city=input("\nDo you wants to see other city weater(yes/no):")
	if next_city=="no":
		break
	

"""To get api key follow the steps
🔹 Step 1: Open the website
            Go to 👉 openweathermap.org
🔹 Step 2: Sign up
          Tap Sign Up
          Enter:
                  Email
                  Password
          Verify your email (important!)
🔹 Step 3: Login
             After verification, login to your account.
🔹 Step 4: Go to API Keys
Tap your profile icon
             Open My API Keys
             You will see a default key 
             copy the key
🕒 Wait 10–15 minutes for activation.
"""
