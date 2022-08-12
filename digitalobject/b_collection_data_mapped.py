import os
import json
import _jsonnet

import settings
settings.init()

from pathlib import Path



template_file = "../templates/digital_object_template.jsonnet"
template = Path(template_file).read_text()
   
def map_collection_data(data,template,dates,places):


    ext_vars = {
        "id"     : data["id"],
        "title"     : data["attributes"]["title"],
        "base_path" : data["attributes"]["base_path"],
        "signature" : data["attributes"]["signature"],
        "oldnr"     : data["attributes"]["oldnr"]
        }

    try:
        dates_id = data["relationships"]["date"]["data"]["id"]

        for date in dates:
            if  date["id"] == dates_id:
                ext_vars["date_start"] = date["attributes"]["date"]
                ext_vars["date_end"] =  date["attributes"]["end_date"]
                ext_vars["date_display"] = date["attributes"]["date_string"]
    except:
        ext_vars["date_start"] = ""
        ext_vars["date_end"] =  ""
        ext_vars["date_display"] = ""

    try:
        place_id = data["relationships"]["place"]["data"]["id"]

        for place in places:
            if  place["id"] == place_id:
                ext_vars["place_id"] = place["id"]
                ext_vars["geonames_id"] = "https://geonames.org/" + place["attributes"]["geonames_id"]
                ext_vars["place_label"] =  place["attributes"]["label"]
                
    except:
        ext_vars["place_id"] = ""
        ext_vars["geonames_id"] = ""
        ext_vars["place_label"] =  ""
    

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
            filename = os.path.basename(file)
            data = json.load(json_file)
            
            data_images = []
            data_dates = []
            data_places = []


            for record in data["included"]:
                if record["type"] == "dates":
                    data_dates.append(record)
                elif record["type"] == "places":
                    data_places.append(record)            

            
            for record in data["data"]:
                if record["type"] == "images" and record["attributes"]["base_path"] == "SGV_10":
                    data_images.append(record)
            
            for record in data_images:
                mapped_collection_data = map_collection_data(record,template, data_dates, data_places)
                filename = str(record["id"]) + ".json"
                print(filename)
                # write linked art to file
                f = open(mapped_collection_data_directory + "/"+ filename , "w")
                f.write(json.dumps(mapped_collection_data,indent=2))
                f.close() 
        
        if filename =="1.json":
            break