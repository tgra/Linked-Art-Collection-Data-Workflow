

import os
import json

import settings
settings.init()

from pathlib import Path


## ===============================================

# read in config
mapped_collection_data_directory        = settings.myVars["mapped_collection_data_directory"]
collection_data_directory               = settings.myVars["collection_data_directory"]
types                                   = settings.myVars["types"]

def map_collection_data(data):

    json = {
        "id": "<<id>>",
        "_label": "<<attributes/title>>",
        "type": "http://vocab.getty.edu/aat/300215302",
        
        "member_of": [{
                "id": "",
                "_label": "<attributes/base_path>",
                "type": "collection"
        }],
        "subject_of": [
            {
            "type": "http://vocab.getty.edu/aat/300264578",
            "_label": "SGV Homepage for PIA ID <<id>> - <<attributes/title>>",
            "access_point_id": ""
        },
        {
            "type" : "iiif",
            "_label" : "IIIF Manifest for PIA ID <<id>> - <<attributes/title>>",
            "access_point_id": "https://iiif.participatory-archives.ch/<ID>/manifest.json"
        }
        ],
        "current_owner": {
            "id": "https://linkedart.participatory-archives.ch/group/42",
            "_label": "SGV Fotoarchiv",
            "type_id": "http://vocab.getty.edu/aat/300343368",
            "type_label": "Photo Archives"
        },
        "created_by": {
            "_label" : "Digitisation of Photograph",
            "used": {
                "_label": "Negative of <<attributes/title>>",
                "width": "",
                "height": "",

                "produced_by_event": {
                    "begin": "",
                    "end": "",
                    "display_title": "",
                    "location": [{
                        "id": "",
                        "_label": ""
                    }],
                    "person": [{
                        "id": "",
                        "_label": ""
                    }]
                    
                        },
                "shows": {
        
                    "_label": "Visual Content of Negative of <<attributes/title>>"}
            }
        },
        
        "identified_by": {

            "names": [
                {
                    "_label": "<<attributes/title>>",
                    "type": {
                        "id": "http://vocab.getty.edu/aat/300404670",
                        "_label": "Owner-Assigned Title"
                    },
                    "language": {
                        "id": "http://vocab.getty.edu/aat/300388344",
                        "_label": "German"
                    }
                }
            ],

            "identifiers": [
                {
                    "value": "<<attributes/oldnr>>",
                    "type": {
                        "id": "http://vocab.getty.edu/aat/300417447",
                        "_label": "Creator-Assigned Number"
                    }
                },
                {
                    "value": "<<attributes/signature>>",
                    "type": {
                        "id": "http://vocab.getty.edu/aat/300312355",
                        "_label": "SGV Signature"
                    }
                },
                {
                    "value": "<<id>>",
                    "type": {
                        "id": "http://vocab.getty.edu/aat/300404621",
                        "_label": "PIA ID"
                    }
                }
            ]
        },
        "access_point": {
            "id": "https://sipi.participatory-archives.ch/<<attributes/base_path>>/<<attributes/signature>>.jp2/full/max/0/default.jpg",
            "_label": "Image in full resolution"
        },
        "iiif_image_api": "https://sipi.participatory-archives.ch/<<attributes/base_path>>/<<attributes/signature>>.jp2/info.json",

        "digitally_shows": {
            "_label": "Visual Content of Digital Positive of <<attributes/title>>",
            "type_id": "",
            "type_label": ""
        }
    }

    # identifier
    json["id"] = data["data"]["id"]

    # label
    json["_label"] = "PIA ID " + data["data"]["id"] + " - " + data["data"]["attributes"]["title"]

    return json

# iterate over files in mapped_collection_data dir
files = Path(collection_data_directory).glob('*')
for file in files:
    filename = os.path.basename(file)
    with open(file) as json_file:
        filename = os.path.basename(file)
        data = json.load(json_file)

        mapped_collection_data = map_collection_data(data)
        
        print(json.dumps(mapped_collection_data,indent=2))
        
        # write linked art to file
        f = open(mapped_collection_data_directory + "/"+ filename , "w")
        f.write(json.dumps(mapped_collection_data,indent=2))
        f.close() 