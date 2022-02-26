import requests

LAT = 19.876165
LNG = 75.343315

parameters = {
    "lat": LAT,
    "lng": LNG,
    "formatted": 0
}

response = requests.get("http://api.open-notify.org/iss-now.json", params=parameters)
data = response.json()  
print(data)

