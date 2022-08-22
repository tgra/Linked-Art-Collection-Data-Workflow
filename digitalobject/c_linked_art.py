import cromulent
import pyld
import os
import json
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

import globalvars
globalvars.init()

import settings
settings.init()


import patterns

from pathlib import Path

from cromulent.model import factory

from os import walk


# ===============================================

# read in config
b_mapped = settings.myVars["b_mapped"]
c_linked_art = settings.myVars["c_linked_art"]

factory.default_lang = settings.myVars["default_lang"]
factory.base_url = settings.myVars["base_url"]
types = globalvars.globalVars["types"]

print(types)



files = []
for (dirpath, dirnames, filenames) in walk(b_mapped):
    files.extend(filenames)
    break
files.sort()

# iterate over files in b_mapped

for file in files:
    filename = os.path.basename(file)

    print(filename)
    with open(b_mapped + '/' + file) as json_file:
        data = json.load(json_file)
        digital_object = patterns.digital_object_pattern(data, types)
        la = factory.toString(digital_object, compact=False)

        # write linked art to file
        f = open(c_linked_art + "/" + filename, "w")
        f.write(la)
        f.close()
