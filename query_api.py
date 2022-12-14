import json
import requests
import sys
import traceback
import yaml
from yaml.loader import SafeLoader

# settings.py in local dir
import settings

[config] = settings.query_api()

# ===============================================
# read in config
with open(config) as f:
    data = yaml.load(f, Loader=SafeLoader)
    config = data[1]

# dir to store collection data files
a_collection = config["directory"] + config["a_collection"]

# number of records to return per page
page_size = config["page_size"]

# default total number of pages to return - actual number will be determined by call to API
total_pages = 1



# URI for PIA API
api_uri = config["pia_api_uri"]
api_include = ""
if config["pia_api_include"] != None:
    api_include = config["pia_api_include"]
# =============================


# QUERY API

# get total number of pages
query_total_pages = api_uri + "?page[number]=1&page[size]=" + str(page_size)
response = requests.get(query_total_pages)
result = response.json()
# get total pages from api call
total_pages = result["meta"]["page"]["lastPage"]
print("total pages: " + str(total_pages))


# construct query to return data
query = api_uri + "?" + api_include + "&page[size]=" + str(page_size)

print("saving files to: " + a_collection)

# iterate through paged records
for page in range(1, total_pages + 1):
   
    # add page number to query
    query1 = query + "&page[number]=" + str(page)
    print('\n' + query1, end='', flush=True)
    # use try statement to pick up errors
    try:
        # query api
        response = requests.get(query1)
        json_data = response.json()

        # write file to collection data dir
        text_file = open(a_collection + "/" + str(page) + ".json", "wt")
        n = text_file.write(json.dumps(json_data, indent=2))
        text_file.close()

    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

print("script completed")
