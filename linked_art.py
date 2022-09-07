from cromulent.model import factory
import os
from os import walk
import json

import yaml
from yaml.loader import SafeLoader


from pathlib import Path

import patterns

# ===============================================
# settings.py in local dir
import settings
[objtype,config_file] = settings.transform()

with open(config_file) as f:
    data = yaml.load(f, Loader=SafeLoader)
    config = data[1]


# dir to store collection data files
directory               = config["directory"]
b_mapped                = directory + config["b_mapped"]
c_linked_art            = directory + config["c_linked_art"]
factory.default_lang    = config["default_lang"]
factory.base_url        = config["base_url"]


globalvars = []
# read in config
with open('globalvars.yaml') as f:
    data = yaml.load(f, Loader=SafeLoader)
    globalvars = data


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
        if objtype == "digitalobject":
            data = patterns.digital_object_pattern(data, globalvars)
        elif objtype == "humanmadeobject":
            data = patterns.humanmadeobject_pattern(data, globalvars)
        elif objtype == "set":
            data = patterns.set_pattern(data, globalvars)

        la = factory.toString(data, compact=False)

        # write linked art to file
        f = open(c_linked_art + '/' + filename, "w")
        f.write(la)
        f.close()
