import requests

api_key = "995bf9ac35bad650f13dd5eed30dcb96"
OWN_endpoint = "https://api.openweathermap.org/data/2.5/forecast"    # first check in browser then paste here because directly you copy from the wedsite and then paste so it's not work properly.

parameters = {
    "lat": 18.520430,
    "lon":73.856743,
    "appid": api_key,
    "cnt": 4,
}
responses = requests.get(OWN_endpoint, params=parameters)
print(responses.status_code)     # It is successful
responses.raise_for_status()
weather_data = responses.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) > 700:
        will_rain = True

if will_rain:
    print("Bring an Umbrella!")


# print(weather_data["list"][0]["weather"][0]["description"])
# for hour_data in weather_data["list"]:
#     print(hour_data["weather"])

# Check result in proper viewer. https://jsonviewer.stack.hu/
# identify weather number from this link https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2