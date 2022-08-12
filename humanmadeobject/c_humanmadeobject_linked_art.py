import cromulent
import pyld
import os
import json
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

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
for root, directories, files in os.walk(mapped_collection_data_directory):
    directories[:] = [d for d in directories if d not in ['example']]
    for file in files:
        filename = os.path.basename(file)
        print(filename)
        with open(mapped_collection_data_directory + '/' + file) as json_file:
            data = json.load(json_file)
            object = patterns.humanmade_object_pattern(data,types)
            la = factory.toString(object, compact=False)

            # write linked art to file
            f = open(linked_art_data_directory + "/"+ filename , "w")
            f.write(la)
            f.close() 