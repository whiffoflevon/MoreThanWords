import requests
import sys 
import json

if len(sys.argv) !=2:
    sys.exit()

response=requests.get("https://itunes.apple.com/search?entity=song&limit=5&term=" + sys.argv[1]) # Making a request to the API) 
o= response.json() # Parsing the JSON response
for i in o["results"]:
    print(i["trackName"] + " by " + i["artistName"] + " is " + str(i["trackPrice"]) + " for " + i["currency"] + ".") # Printing the results