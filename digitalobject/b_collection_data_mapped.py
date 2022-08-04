import os
import json
import json
import _jsonnet

import settings
settings.init()

from pathlib import Path



template_file = "./templates/digital_object_template.jsonnet"
template = Path(template_file).read_text()
   
def map_collection_data(data,template):

    

    ext_vars = {
        "id"     : data["id"],
        "title"     : data["attributes"]["title"],
        "base_path" : data["attributes"]["base_path"],
        "signature" : data["attributes"]["signature"],
        "oldnr"     : data["attributes"]["oldnr"]
        }

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
files = Path(collection_data_directory).glob('1.json')


for file in files:
    filename = os.path.basename(file)
    with open(file) as json_file:
        filename = os.path.basename(file)
        data = json.load(json_file)
        

        for record in data["data"]:
            
            mapped_collection_data = map_collection_data(record,template)
            filename = str(record["id"]) + ".json"
            print(filename)
            # write linked art to file
            f = open(mapped_collection_data_directory + "/"+ filename , "w")
            f.write(json.dumps(mapped_collection_data,indent=2))
            f.close() 
            