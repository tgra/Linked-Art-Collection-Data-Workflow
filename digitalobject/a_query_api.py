import inspect
import json
import os
from pathlib import Path
import requests
import sys
import traceback

'''
This script queries the PIA JSON API using variables in settings.py and writes the JSON data returned to a local directory

'''



# allow python from parent directory to be included
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

# import setting variables in settings.py
import settings
settings.init()



## ===============================================

# read in config

# dir to store collection data files 
a_collection        = settings.myVars["a_collection"]

# number of records to return per page
page_size           = settings.myVars["page_size"]

# total number of pages to return
total_pages         = 1

# URI for PIA API
api_uri             = settings.myVars["pia_api_uri"]

# API URI

# get total number of pages
query           =  api_uri + "?page[number]=1&page[size]=" + str(page_size)
response        = requests.get(query)
result          = response.json()
total_pages     = result["meta"]["page"]["lastPage"]

# now query to return data
query           = api_uri + "?include=collections,date,place&page[size]=" + str(page_size)

# iterate through paged records
for page in range(1, total_pages + 1):
    # add page number to query
    query = query + "&page[number]=" + str(page)
    
    # use try statement to pick up errors
    try:
        # query api
        response = requests.get(query)
        json_data = response.json()

        # write file to collection data dir
        text_file = open( a_collection + "/" + str(page) + ".json", "wt")
        n = text_file.write(json.dumps(json_data, indent=2))
        text_file.close()
    except Exception as e: 
       
        traceback.print_exc()
        break
        

print("script completed")    
        