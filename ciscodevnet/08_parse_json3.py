import urllib.parse
import requests


main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "59tauwUulKkHe4HGiIJRwm1GeK1haAj4"

while True:
    orig = input("Please, enter starting point: ")
    dest = input("Please, enter destination: ")
    if 
    url = main_api + urllib.parse.urlencode({'key': key, 'from': orig, 'to': dest})
    print("URL: " + (url))

    json_data = requests.get(url).json()
    json_status = json_data['info']['statuscode']

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")

