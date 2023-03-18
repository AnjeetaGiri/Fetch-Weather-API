
import requests
API_Key="aea81102b99930f177dc9a7e6d3ba6a4"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
city=input("Enter a city name:")
request_url = f"{BASE_URL}?appid={API_Key}&q={city}"
response=requests.get(request_url)
if response.status_code==200:
    data=response.json()
    print(data)
    weather=data['weather'][0]['description']
    
    temperature=round(data["main"]["temp"]-273.15,2)
    print("Weather:",weather)
    print("Temperature:",temperature,"celcius")
else:
    print("An error occured")    