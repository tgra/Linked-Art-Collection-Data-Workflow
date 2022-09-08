"""
## Introduction
The query_api.py file queries the PIA JSON API and writes the JSON files returned to a local directory, ready for transformation to Linked Art JSON-LD.
A .yaml file is used for script variables. The filepath for the .yaml file is specified as a script argument --config

## Example settings.yaml  file
A settings.yaml file is specified in the script argument --config. 
An example config file can be viewed at [example settings.yaml](/digitalobject/settings.yaml)

Example content:
```yaml
- - - # settings for digital object
- settings:
  default_lang        : en
  base_url            : https://linkedart.participatory-archives.ch/
  pia_api_uri         : https://data.participatory-archives.ch/api/v1/images
  pia_api_include     : include=collections,date,place
  page_size           : 500
  directory           : digitalobject/
  a_collection        : data/a_collection
  b_mapped            : data/b_mapped
  c_linked_art        : data/c_linked_art
  template            : template.jsonnet
...
```

The query URL for the PIA API query is contstructed using 'pia_api_url' and 'pia_api_include' in the settings.yaml file.

JSON files are written to a local directory, with the filepath constructed using the 'directory', 'a_collection' and 'page_size' variables in the setting.yaml file.

## Files
- query_api.py - main script
- settings.py - use function 'query_api()' to check that the correct script arguments have been provided

# Help
The following will provide information about arguments to use with the script.
```
python3 query_api.py -h 
```

# Example command
```python
query_api.py  --config <config-file>
```
e.g.
```python
python3 query_api.py --config ./digitalobject/settings.yaml 
```
"""


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
query = api_uri + "?page[number]=1&page[size]=" + str(page_size)
response = requests.get(query)
result = response.json()

# get total pages from api call
total_pages = result["meta"]["page"]["lastPage"]


# construct query to return data
query = api_uri + "?" + api_include + "&page[size]=" + str(page_size)

print("total pages: " + str(total_pages))
print("saving files to: " + a_collection)


# iterate through paged records
for page in range(1, total_pages + 1):
    print(str(page) + '.', end='', flush=True)
    # add page number to query
    query = query + "&page[number]=" + str(page)

    # use try statement to pick up errors
    try:
        # query api
        response = requests.get(query)
        json_data = response.json()

        # write file to collection data dir
        text_file = open(a_collection + "/" + str(page) + ".json", "wt")
        n = text_file.write(json.dumps(json_data, indent=2))
        text_file.close()

    except Exception as e:
        traceback.print_exc()
        sys.exit(1)

print("script completed")
