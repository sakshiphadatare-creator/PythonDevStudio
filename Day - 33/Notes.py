import requests
from datetime import datetime
MY_LAT = 51.507351
MY_LONG = -0.127758

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,    # keys write properly
    "formatted": 0
}

# https://sunrise-sunset.org/api
response = requests.get(url="https://api.sunrise-sunset.org/json",params= parameters) #url = uniform resource locator
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

#print(sunrise.split("T")[1].split(":")[0])     #  T is remove and separate by ","
print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)






# responses = requests.get(url="http://api.open-notify.org/iss-now.json")    # requests to external system  iss = International Space Station
# responses.raise_for_status()     # This will shout if something went wrong!
#
# data = responses.json()  # we use javascript object notation also known as json because of I try to print responses aspected result not required
# # print(data)                # check the result to this link https://www.latlong.net/Show-Latitude-Longitude.html
#
# longitude = data["iss_position"]["longitude"]
# latitude = data['iss_position']["latitude"]
# #print((longitude, latitude))
#
# iss_position = (longitude, latitude)
# print(iss_position)


# Raise_for_status

# You order juice online. If the delivery is successful, great—you drink it. But if the delivery fails
 # (like the store is closed or the juice is out of stock), you want to know something went wrong, right?
# If everything is okay (like the website responds with a “200 OK”), it stays quiet.
# If something goes wrong (like “404 Not Found” or “500 Server Error”), it raises an error to let you know.



# 400 Client Error: Bad Request for url: It means The website didn’t understand what you asked for