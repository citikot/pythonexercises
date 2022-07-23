import urllib.parse
import requests


main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Kyiv"
dest = "Lviv"
key = "59tauwUulKkHe4HGiIJRwm1GeK1haAj4"

url = main_api + urllib.parse.urlencode({'key': key, 'from': orig, 'to': dest})


json_data = requests.get(url).json()

print("URL: " + (url))

json_status = json_data['info']['statuscode']

if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")
