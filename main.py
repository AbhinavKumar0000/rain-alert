import requests
from twilio.rest import Client

endpoint = "https://pro.openweathermap.org/data/2.5/forecast"
api_key = "1b623690d1841bd2d55b902d99eabfbf"
account_sid = "ACc125cd726cfcc7bc34a303e30db39c68"
auth_token = "da90b460d15d5435d43365b16683747f"
# LAT = 23.205011
# LONG = 77.085075
LAT = -9.3167 #currently raining
LONG = 132.45
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



