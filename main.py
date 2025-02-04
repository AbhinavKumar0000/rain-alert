import requests
from twilio.rest import Client

endpoint = "https://pro.openweathermap.org/data/2.5/forecast"
api_key = "" # Enter your API KEY here
account_sid = "" #Enter you acc SID here
auth_token = "" # Enter your authentication token here
LAT = #Enter your lattitude here
LONG = #Enter your longitude here
# LAT = -9.3167 #use this coordinates for checking this code (currently raining here)
# LONG = 132.45
parameters = {
    "lat": LAT,
    "lon": LONG,
    "cnt": 4,
    "appid": api_key,
}
response = requests.get(endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid,auth_token)
    message = client.messages.create(
        body="Bring an Umbrella☔... it might rain☁️",
        from_="+18596970391",
        to="+918383951265",
    )
    print(message.status)



