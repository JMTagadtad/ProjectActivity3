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

print ("GROUP 7 - PROJECT # 4\n")
print ("IP ADDRESS GEOLOCATION INFO:")
print ("===================================")

# Title for each category (Added category: Postal Code, Time Zone, Languages)
category = ["IP Address", "Version", "City", "Region", "Country", "Postal Code", "Time Zone", "Continent Code", "Currency", "Languages","Autonomous System Number", "ISP"]

# fetch json data from the api
json_categories = ["ip", "version", "city", "region", "country_name", "postal", "timezone", "continent_code", "currency", "languages", "asn", "org"]

#display output
for i in range(len(category)):
    print(category[i] +  ": " + json_data[json_categories[i]])
    print ("===================================")