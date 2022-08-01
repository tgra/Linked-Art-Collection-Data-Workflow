
import cromulent
import pyld


from cromulent.model import factory, Group, DigitalObject
from cromulent.vocab import Type, Set, LinguisticObject, Name, InformationObject, Creation, VisualItem, Identifier
from cromulent.vocab import Production, HumanMadeObject, Dimension, MeasurementUnit,TimeSpan, Place, Person, Language, DigitalService

"""

* id
* type
* _label
* classified_as type
* member_of collection
* subject_of 
  * linguistic object 
    * digitally_carried_by digital object
    * identified_by
    * conforms_to
    * access_point
* current_owner
* created_by
  * used_specific_object
    * classified_as
    * dimension
    * produced_by production
      * took_place_at
      * carried_out_by
    * shows
* digitally_shows
* identified_by
* access_point
* digitally_available_via
"""

types = {
    "http://vocab.getty.edu/aat/300215302" :{ 
        "_label": "Digital Image"
    },
    "http://vocab.getty.edu/aat/300025976" : { 
        "_label": "Collection"
        },
    "http://vocab.getty.edu/aat/300264578":{
        "_label": "Web Page"
    },
    "http://vocab.getty.edu/aat/300055647":{ 
        "_label": "Width"
    },
    "http://vocab.getty.edu/aat/300379098":{
        "_label": "Height"
    },
    "http://vocab.getty.edu/aat/300379098":{
        "_label": "Centimetres"
    },
    "http://vocab.getty.edu/aat/300379098":{
        "_label": "Display Title"
    }

}


data = {
        "id": "12033",
        "_label": "PIA ID 12033 - [Schwyzer Fasnacht]",
        "type": "http://vocab.getty.edu/aat/300215302",
        "member_of": [{
            "id": "12",
             "_label": "SGV_12 (Ernst Brunner)",
             "type": "collection"
        }],
        "subject_of": [{
            "type": "http://vocab.getty.edu/aat/300264578",
            "_label": "SGV Homepage for PIA ID 12033 - [Schwyzer Fasnacht]",
            "access_point_id": "https://archiv.sgv-sstp.ch/resource/422236"
        },
        {
            "type": "iiif",
            "_label": "IIIF Manifest for PIA ID 12033 - [Schwyzer Fasnacht]",
            "access_point_id": "https://iiif.participatory-archives.ch/12033/manifest.json",   
          }
        ],
        "current_owner": {
            "id": "",
            "_label": "",
            "type_id": "",
            "type_label": ""
        },
        "created_by": {
            "_label": "",
            "used": {
                "label": "",
                "type_id": "",
                "type_label": "",
                "dimension" : {
                    "type" : "",
                    "value" : "",
                    "unit": "http://vocab.getty.edu/aat/300379098"
                },
            
            "produced_by":{
            "timespan" : {
                "name": {
                    "type" : "http://vocab.getty.edu/aat/300379098",
                    "content" : "1937"
                },
                "begin": "",
                "end": ""
            },
            "took_place_at": {
                "id": "",
                "_label": ""
            },
            "carried_out_by": {
                "id": "",
                "_label": ""
                }
        },
        "shows": {
            "_label": ""
        }
            }

    },
    "digitally_shows": {},
"identified_by": {},
"access_point": {},
"digitally_available_via" : {}
    }
        

factory.default_lang = "en"
factory.base_url="https://linkedart.participatory-archives.ch/"

# identifier and type
digital_object_1 = DigitalObject(ident=data["id"]) 

# label
digital_object_1._label = data["_label"]

# classified_as
type = types[data["type"]]
id = data["type"]
label = type["_label"]

digital_object_1.classified_as = Type(ident=id, label=label)

# member_of collection

collection = data["member_of"][0]
id = collection["id"]
label = collection["_label"]

digital_object_1_collection = Set(ident=id,label=label)

type = types["http://vocab.getty.edu/aat/300025976"]
id = "http://vocab.getty.edu/aat/300025976"
label = type["_label"]

digital_object_1_collection.classified_as = Type(ident=id, label=label)

digital_object_1.member_of = digital_object_1_collection

# subject_of web page
data_web_page = data["subject_of"][0]
label = data_web_page["_label"]
access_point_id = data_web_page["access_point_id"]
linguistic_object_1 =  LinguisticObject(ident="", label=label)

digital_object_2 = DigitalObject(ident="", label=label)
digital_object_2.format = "text/html"
digital_object_2.access_point = DigitalObject(ident=access_point_id)
digital_object_2.classified_as = Type(ident="http://vocab.getty.edu/aat/300264578", label="Web Page")
digital_object_2.identified_by = Name(ident="", label=label)

linguistic_object_1.digitally_carried_by = digital_object_2

digital_object_1.subject_of = linguistic_object_1


# subject_of iiif

data_iiif = data["subject_of"][1]
label = data_iiif["_label"]
access_point_id = data_iiif["access_point_id"]
linguistic_object_2 =  LinguisticObject(ident="", label=label)

digital_object_3 = DigitalObject(ident="", label=label)
digital_object_3.format = "application/ld+json"
digital_object_3.access_point = DigitalObject(ident=access_point_id)
digital_object_3.conforms_to = InformationObject(ident="http://iiif.io/api/presentation/3/context.json", label="")
digital_object_3.identified_by = Name(ident="", label=label)

linguistic_object_2.digitally_carried_by = digital_object_3

digital_object_1.subject_of = linguistic_object_2

# not supported in cromulent
#digital_object_1.current_owner = Group(ident="https://linkedart.participatory-archives.ch/group/42", label="SGV Fotoarchiv")

# creation event
creation_event_1 = Creation(ident="", label="Digitisation of Photograph")


# negative
HumanMadeObject_1 =  HumanMadeObject(ident="",label="Negative of [Schwyzer Fasnacht]")

type_1 = Type(ident="http://vocab.getty.edu/aat/300128343", label="Black and White Negative")
type_1.classified_as = Type(ident="http://vocab.getty.edu/aat/300435443", label="Type of Work")

HumanMadeObject_1.classified_as = type_1

# measurement dimension

# width
dimension_1= Dimension(ident="", label="")
dimension_1.classified_as = Type(ident="http://vocab.getty.edu/aat/300055647", label="Width")
dimension_1.value = 6
dimension_1.unit = MeasurementUnit(label="Centimetres", id="http://vocab.getty.edu/aat/300379098")

# height
dimension_2= Dimension(ident="", label="")
dimension_2.classified_as = Type(ident="http://vocab.getty.edu/aat/300055644", label="Height")
dimension_2.value = 6
dimension_2.unit = MeasurementUnit(label="Centimetres", id="http://vocab.getty.edu/aat/300379098")

HumanMadeObject_1.dimension = dimension_1
HumanMadeObject_1.dimension = dimension_2


# creation and production 
creation_event_1.used_specific_object = HumanMadeObject_1
digital_object_1.created_by = creation_event_1

production_1 = Production(ident="", label="")

type_1 = Type(ident="http://vocab.getty.edu/aat/300404669", label="Display Title")

name_1 = Name(ident="", label="")
name_1.content = "1937"
name_1.classified_as = type_1

timespan_1 = TimeSpan(ident="", label="")
timespan_1.identified_by = name_1
timespan_1.begin_of_the_begin = "1937-01-01T00:00:00Z"
timespan_1.end_of_the_end = "1937-12-31T23:59:59Z"

production_1.timespan = timespan_1
production_1.took_place_at = Place(ident="https://linkedart.participatory-archives.ch/place/2", label="Schwyz")
production_1.carried_out_by = Person(ident="https://linkedart.participatory-archives.ch/person/12345", label="Ernst Brunner")


HumanMadeObject_1.produced_by = production_1
HumanMadeObject_1.shows = VisualItem(ident="", label="Visual Content of Negative of [Schwyzer Fasnacht]")


visual_item_1 = VisualItem(ident="", label='Visual Content of Digital Positive of [Schwyzer Fasnacht]')
visual_item_1.represents_instance_of_type = Type(ident="http://vocab.getty.edu/aat/300164207", label="Carnival")
digital_object_1.digitally_shows = visual_item_1

# identifiers
name_1 = Name(ident="",label="[Schwyzer Fasnacht]")
name_1.classified_as = Type(ident="http://vocab.getty.edu/aat/300404670", label="Owner-Assigned Title")
name_1.language = Language(ident="http://vocab.getty.edu/aat/300388344", label="German")

identifier_1 = Identifier(content="AA 1", ident="")
identifier_1.classified_as = Type(ident="http://vocab.getty.edu/aat/300417447", label="Creator-Assigned Number")

identifier_2 = Identifier(content="SGV_12N_00001", ident="")
identifier_2.classified_as = Type(ident="http://vocab.getty.edu/aat/300312355", label="SGV Signature")

identifier_3 = Identifier(content="12033", ident="")
identifier_3.classified_as = Type(ident="http://vocab.getty.edu/aat/300404621", label="PIA ID")

digital_object_1.identified_by = name_1
digital_object_1.identified_by = identifier_1
digital_object_1.identified_by = identifier_2
digital_object_1.identified_by = identifier_3

# access point
digital_object_1.access_point = DigitalObject(ident="https://sipi.participatory-archives.ch/SGV_12/SGV_12N_00001.jp2/full/max/0/default.jpg", 

    label="Image in full resolution" )

# digitally available via
digital_service_1 = DigitalService(label="IIIF Image API")
digital_service_1.format = "application/ld+json"
digital_service_1.access_point = DigitalObject(id="https://sipi.participatory-archives.ch/SGV_12/SGV_12N_00001.jp2/info.json")
digital_service_1.conforms_to = InformationObject(ident="http://iiif.io/api/image/3/context.json")

digital_object_1.digitally_available_via = digital_service_1

# print final LA
print(factory.toString(digital_object_1, compact=False))

