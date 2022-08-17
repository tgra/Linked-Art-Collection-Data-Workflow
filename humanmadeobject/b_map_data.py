import _jsonnet
import inspect
import json
import os
from os import walk
from pathlib import Path
import sys


# allow python from parent directory to be included
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

import settings
settings.init()


# ======================================

# read in config
a_collection    = settings.myVars["a_collection"]
b_mapped        = settings.myVars["b_mapped"]
template        = Path(settings.myVars["humanmadeobject_template"]).read_text() # jsonnet template for intermediate JSON data file


# ======================================



   
def map_collection_data(data,template,dates,places,collections):

   
    ext_vars = {
        "id"            : data["id"],
        "title"         : data["attributes"]["title"],
        "base_path"     : data["attributes"]["base_path"],
        "signature"     : data["attributes"]["signature"],
        "oldnr"         : data["attributes"]["oldnr"],
        "salsah_id"     : data["attributes"]["salsah_id"],
        
        "date_start"    : "",
        "date_end"      :  "",
        "date_display"  :  "",

        "place_id"      : "",
        "geonames_id"   : "",
        "place_label"   :  "",

        "collection_id" : "",
        "collection_label"  : ""
        }

    try:
        dates_id = data["relationships"]["date"]["data"][0]["id"]

        for date in dates:
            if  date["id"] == dates_id:
                ext_vars["date_start"] = date["attributes"]["date"]
                ext_vars["date_end"] =  date["attributes"]["end_date"]
                ext_vars["date_display"] = date["attributes"]["date_string"]
    except: 
        pass

    try:
        place_id = data["relationships"]["place"]["data"][0]["id"]

        for place in places:
            if  place["id"] == place_id:
                ext_vars["place_id"] = place["id"]
                ext_vars["geonames_id"] = "https://geonames.org/" + place["attributes"]["geonames_id"]
                ext_vars["place_label"] =  place["attributes"]["label"]
                
    except:
        pass

    
    try:
        collection_id = data["relationships"]["collections"]["data"][0]["id"]
        
        for collection in collections:
            if  collection["id"] == collection_id:
                ext_vars["collection_id"] = collection_id
                ext_vars["collection_label"] =   collection["attributes"]["label"]
    except:
        pass
                
    for k , val in ext_vars.items():
        if val is None:
            ext_vars.update({k: ""})

    json_str = _jsonnet.evaluate_snippet("snippet", template, ext_vars=ext_vars)

    return json.loads(json_str)


## ===============================================

files = []
for (dirpath, dirnames, filenames) in walk(a_collection):
    files.extend(filenames)
    break
files.sort()

# iterate over files in collection_data dir
for file in files:
    filename = os.path.basename(file)
    print(filename)  

    with open(a_collection + '/' + file) as json_file:
        data = json.load(json_file)
            
        data_images = []
        data_dates = []
        data_places = []
        data_collections = []

        for record in data["included"]:
            if record["type"] == "dates":
                data_dates.append(record)
            elif record["type"] == "places":
                data_places.append(record) 
            elif record["type"] == "collections":
                data_collections.append(record)           

        for record in data["data"]:
            if record["type"] == "images" and record["attributes"]["base_path"] == "SGV_12":
                data_images.append(record)

        for record in data_images:
            mapped_collection_data = map_collection_data(record,template, data_dates, data_places, data_collections)
                
            # write intermediate json data format to file
            f = open(b_mapped + "/"+ str(record["id"]) + ".json" , "w")
            f.write(json.dumps(mapped_collection_data,indent=2))
            f.close() 
            print('.', end='', flush=True)
    
    # comment/remove following line if you want to iterate over all collection data files in a_collection
    