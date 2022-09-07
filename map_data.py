import json
import os
from os import walk
from pathlib import Path
import yaml
from yaml.loader import SafeLoader

# mapping functions in local dir
import map_data_func

# settings.py in local dir
import settings
[objtype, config_file, template] = settings.map_data()

# ===============================================
# READ IN CONFIG

with open(config_file) as f:
    data = yaml.load(f, Loader=SafeLoader)
    config = data[1]

directory = config["directory"]
a_collection = directory + config["a_collection"] # dir to store collection data files
b_mapped = directory + config["b_mapped"] # dir to store mapped data
template = Path(template).read_text() # jsonnet template for intermediate JSON data file


## ===============================================

# ITERATE OVER FILES IN COLLECTION DATA DIR

files = []
for (dirpath, dirnames, filenames) in walk(a_collection):
    files.extend(filenames)
    break
files.sort()

for file in files:
    filename = os.path.basename(file)
    print(filename)  
    # open file 
    with open(a_collection + '/' + file) as json_file:
        filename = os.path.basename(file)
        # load data into python dict
        data = json.load(json_file)
            
        # create lists for additional image, date and place data identified in record
        
        mapped_data = None

        # iterate over included data and append  date, collection and place data to lists
        if "included" in data:
            include_data = []
            data_dates  = []
            data_places = []
            data_collections = []

            for record in data["included"]:
                if record["type"] == "dates":
                    data_dates.append(record)
                elif record["type"] == "places":
                    data_places.append(record) 
                elif record["type"] == "collections":
                    data_collections.append(record)            
            include_data = [data_dates,data_places,data_collections]

        # map data for digital object and humanmadeobject
        if objtype in ["humanmadeobject","digitalobject"]:
            data_images = []
            for record in data["data"]:
                if record["type"] == "images":
                    if objtype == "digitalobject" and record["attributes"]["base_path"] == "SGV_10":
                        data_images.append(record)
                    elif objtype == "humanmadeobject" and record["attributes"]["base_path"] == "SGV_12":
                        data_images.append(record)
            for record in data_images:
                json_data = map_data_func.images(record,template, include_data)
                map_data_func.save_file(json_data,b_mapped, record["id"])
        
        # map collection data
        if objtype == 'set':
            for record in data["data"]:
                if record["type"] == "collections":
                    json_data = map_data_func.set(record,template)
                    map_data_func.save_file(json_data, b_mapped, record["id"])



