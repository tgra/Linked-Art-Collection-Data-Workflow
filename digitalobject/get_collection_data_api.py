import requests
import json
import settings
settings.init()

from pathlib import Path


## ===============================================

# read in config
collection_data_directory        = settings.myVars["collection_data_directory"]


records_page = 500
total_pages = 0

uri     =  "https://data.participatory-archives.ch/api/v1/images?page[number]=1&page[size]=" + str(records_page)
response        = requests.get(uri)
json_data       = response.json()

total_pages = json_data["meta"]["page"]["lastPage"]

uri = "https://data.participatory-archives.ch/api/v1/images?include=collections,date,place&page[size]=" + str(records_page)

for page in range(1, 1 + 1):
    query = uri + "&page[number]=" + str(page)
    
    try:
        response = requests.get(query)
        print(query)
        print(response)
        json_data = response.json()
        text_file = open( collection_data_directory + "/" + str(page) + ".json", "wt")
        n = text_file.write(json.dumps(json_data, indent=2))
        text_file.close()
    except:
        print("error occurred")
        print(response)
        print("query:" + query)
        break
        