import urllib.request
import requests

api = "https://ipapi.co/"

ext_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

url = api + ext_ip + "/json"

json_data = requests.get(url).json()

category = ["IP Address", "Version", "City", "Region", "Country"]
json_categories = ["ip", "version", "city", "region", "country_name"]