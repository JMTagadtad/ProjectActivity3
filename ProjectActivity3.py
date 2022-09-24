import urllib
import requests

#chosen REST api
api = "https://ipapi.co/"

# discover external ip address of router
ext_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

# url of the chosen api & external ip 
url = api + ext_ip + "/json"

# fetch json data from api and external ip
json_data = requests.get(url).json()

print ("GROUP 7 - PROJECT # 3\n")

# Title for each category
category = ["IP Address", "Version", "City", "Region", "Country", "Continent Code", "Currency", "Autonomous System Number", "ISP"]

# fetch json data from the api
json_categories = ["ip", "version", "city", "region", "country_name", "continent_code", "currency", "asn", "org"]

#display output
for i in range(len(category)):
    print(category[i] +  ": " + json_data[json_categories[i]])
    print ("===================================")