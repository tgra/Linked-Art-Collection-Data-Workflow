
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
template        = Path(settings.myVars["template"]).read_text() # jsonnet template for intermediate JSON data file


# ======================================

'''
name:
map_collection_data

purpose:
function to map collection data to intermediate JSON data file using jsonnet template


arguments:
- data - collection data json
- template - jsonnet template
- dates - relevant dates in json from collection data  
- places - relevant places in json from collection data

'''

def map_collection_data(data,template):

# ext_vars dictionary holds vars from the collection data record
# In jsonnet it's not possible to test for the existence of an external variables dynamically, 
# therefore all variables need to be set, even if no data available
# ref https://jsonnet.org/ref/language.html

    ext_vars = {
        "id"            : data["id"],
        "label"         : data["attributes"]["label"],
        "signature"     : data["attributes"]["signature"],
        "salsah_id"     : data["attributes"]["salsah_id"],
        "description"     : data["attributes"]["description"]
        }

    
    # iterate through ext_vars - if any values == None, replace with empty string
    for k , val in ext_vars.items():
        if val is None:
            ext_vars.update({k: ""})
    
    # use jsonnet to populate template with vars from ext_vars python dict
    json_str = _jsonnet.evaluate_snippet("snippet", template, ext_vars=ext_vars)

    # return json string as python dictionary
    return json.loads(json_str)


## ===============================================

# iterate over files in a_collection data dir

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
        data_collections = []
        
        # iterate over data and get only digital images, identified by SGV_10 base_path value, and append to data_images list
        for record in data["data"]:
            if record["type"] == "collections":
                data_collections.append(record)
            
        # iterate over collections data and map to intermediate JSON data format using jsonnet template
        for record in data_collections:
            mapped_collection_data = map_collection_data(record,template)

            # write intermediate json data format to file
            f = open(b_mapped + "/"+ str(record["id"]) + ".json" , "w")
            f.write(json.dumps(mapped_collection_data,indent=2))
            f.close() 
            print('.', end='', flush=True)
        
    # comment/remove following line if you want to iterate over all collection data files in a_collection
    #break