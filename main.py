import os
import requests
from twilio.rest import Client

auth_token=os.environ.get("AUTH_TOKEN")
account_sid=os.environ.get("ACCOUNT_SID")



api_key=os.environ.get("API_KEY")

#
wea_endpoint="https://api.openweathermap.org/data/2.5/forecast"



wea_parameter={
    "appid":api_key,
    "lat":22.396427,
    "lon":114.109497,
    "cnt":4,
}



data=requests.get(wea_endpoint,params=wea_parameter)
print(data.status_code)
data.raise_for_status()
weather_data=data.json()

will_rain=False
for x in weather_data["list"]:
    weather_id=(x["weather"][0]["id"])
    if weather_id<700:
        will_rain=True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today, remember to bring a umbrella",
        from_="+16203509797",
        to="+85259839097",
    )
    print(message.status)
