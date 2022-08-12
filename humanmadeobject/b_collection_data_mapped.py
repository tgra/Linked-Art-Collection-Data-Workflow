import os
import json
import _jsonnet
import os
import sys
import inspect

# allow python from parent directory to be included
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 


import settings
settings.init()

from pathlib import Path



template_file = "../templates/humanmadeobject_template.jsonnet"
template = Path(template_file).read_text()
   
def map_collection_data(data,template,dates,places,collections):


    ext_vars = {
        "id"            : data["id"],
        "title"         : data["attributes"]["title"],
        "base_path"     : data["attributes"]["base_path"],
        "signature"     : data["attributes"]["signature"],
        "oldnr"         : data["attributes"]["oldnr"],
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

# read in config
mapped_collection_data_directory        = settings.myVars["mapped_collection_data_directory"]
collection_data_directory               = settings.myVars["collection_data_directory"]

# iterate over files in collection_data dir

for root, directories, files in os.walk(collection_data_directory):
    directories[:] = [d for d in directories if d not in ['example']]

    for file in files:
        filename = os.path.basename(file)
        
        with open(collection_data_directory + '/' + file) as json_file:
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
                
                id = record["id"]
                print(id)
                filename = str(id) + ".json"
                
                # write linked art to file
                f = open(mapped_collection_data_directory + "/"+ filename , "w")
                f.write(json.dumps(mapped_collection_data,indent=2))
                f.close() 
        