
import cromulent
import pyld
import os
import json

import settings
settings.init()

import patterns

from pathlib import Path

from cromulent.model import factory

## ===============================================

# read in config
mapped_collection_data_directory        = settings.myVars["mapped_collection_data_directory"]
linked_art_data_directory               = settings.myVars["linked_art_data_directory"]
factory.default_lang                    = settings.myVars["default_lang"]
factory.base_url                        = settings.myVars["base_url"]
types                                   = settings.myVars["types"]

# iterate over files in mapped_collection_data dir
files = Path(mapped_collection_data_directory).glob('*')
for root, dirs, files in os.walk(mapped_collection_data_directory):
    if dirs == "example":
        continue
    for file in files:
        filename = os.path.basename(file)
        print(filename)
        with open(mapped_collection_data_directory + '/' + file) as json_file:
            data = json.load(json_file)
            digital_object = patterns.digital_object_pattern(data,types)
            la = factory.toString(digital_object, compact=False)

            # write linked art to file
            f = open(linked_art_data_directory + "/"+ filename , "w")
            f.write(la)
            f.close() 