import urllib.request
import requests

#chosen REST api
api = "https://ipapi.co/"

#discover external ip address of router 
ext_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

#url of the chosen api & external ip
url = api + ext_ip + "/json"

#fetch json data from api and external ip
json_data = requests.get(url).json()

#title for each category
category = ["IP Address", "Version", "City", "Region", "Country"]

#fetch json data from the api
json_categories = ["ip", "version", "city", "region", "country_name"]

#display output
for i in range(len(category)):
    print(category[i] + ": " + json_data[json_categories[i]])