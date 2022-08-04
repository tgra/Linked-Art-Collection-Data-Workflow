
import cromulent
import pyld
import os
import json

from cromulent.model import factory, Group, DigitalObject
from cromulent.vocab import Type, Set, LinguisticObject, Name, InformationObject, Creation, VisualItem, Identifier, Production, HumanMadeObject, Dimension, MeasurementUnit, TimeSpan, Place, Person, Language, DigitalService

#==========================

def digital_object_pattern(data,types):

    id                                      = data["type"]
    label                                   = data["_label"]
    # identifier and label
    digital_object                          = DigitalObject(ident=id, label=label)

    # classified_as
    digital_object.classified_as            = type_pattern(id, types)

    # member_of collection
    digital_object.member_of                = collection_pattern(data, types)

    # subject_of web page
    digital_object.subject_of               = web_page_pattern(data["subject_of"][0], types)

    # subject_of iiif
    digital_object.subject_of               = iiif_pattern(data["subject_of"][1], types)

    # not supported in cromulent
    # digital_object_1.current_owner        = Group(ident="", label="")

    # creation and production
    digital_object.created_by               = creation_pattern(data["created_by"], types)

    # digitally_shows
 #   if "digitally_shows" in data :
      #  digital_object.digitally_shows          = digitally_shows_pattern(data["digitally_shows"], types)

    # identifiers
    for name_data in data["identified_by"]["names"]:
        digital_object.identified_by        = name_pattern(name_data, types)

    for id_data in data["identified_by"]["identifiers"]:
        digital_object.identified_by        = identifier_pattern(id_data, types)

    # access point
    digital_object.access_point             = DigitalObject(ident=data["access_point"]["id"],label=data["access_point"]["_label"])

    # digitally available via
    digital_object.digitally_available_via  = digital_service_pattern(data, types)

    return digital_object

#==================================



def type_pattern(id, types):
    type_selected = types[id]
    label = type_selected["_label"]
    type = Type(ident=id, label=label)

    return type

def collection_pattern(data, types):

    id = data["id"]
    label = data["_label"]
    collection_type_id = "http://vocab.getty.edu/aat/300025976"

    collection = Set(ident=id, label=label)
    collection.classified_as = type_pattern(collection_type_id, types)

    return collection


def web_page_pattern(data, types):

    label = data["_label"]
    access_point_id = data["access_point_id"]
    web_page_id = "http://vocab.getty.edu/aat/300264578"

    digital_object = DigitalObject(ident="", label=label)
    digital_object.identified_by = Name(ident="", label=label)
    digital_object.format = "text/html"
    digital_object.access_point = DigitalObject(ident=access_point_id)
    digital_object.classified_as = type_pattern(web_page_id, types)

    linguistic_object = LinguisticObject(ident="", label=label)
    linguistic_object.digitally_carried_by = digital_object

    return linguistic_object


def iiif_pattern(data, types):

    label = data["_label"]
    access_point_id = data["access_point_id"]
    iiif_id = "http://iiif.io/api/presentation/3/context.json"

    digital_object = DigitalObject(ident="", label=label)
    digital_object.format = "application/ld+json"
    digital_object.access_point = DigitalObject(ident=access_point_id)
    digital_object.conforms_to = InformationObject(ident=iiif_id, label="")
    digital_object.identified_by = Name(ident="", label=label)

    linguistic_object = LinguisticObject(ident="", label=label)
    linguistic_object.digitally_carried_by = digital_object

    return linguistic_object


def negative_pattern(data, types):

    label = data["_label"]
    negative_type_id = "http://vocab.getty.edu/aat/300128343"
    work_type_id = "http://vocab.getty.edu/aat/300435443"

    # negative
    hmo = HumanMadeObject(ident="", label=label)
    type = type_pattern(negative_type_id, types)
    type.classified_as = type_pattern(work_type_id, types)
    hmo.classified_as = type

    # measurement dimension

    width_type_id = "http://vocab.getty.edu/aat/300055647"

    # width
    width = Dimension(ident="", label="")
    width.classified_as = type_pattern(width_type_id, types)
    width.value = data["width"]
    width.unit = MeasurementUnit(
        id="http://vocab.getty.edu/aat/300379098", label="Centimetres")

    # height
    height_type_id = "http://vocab.getty.edu/aat/300055644"

    height = Dimension(ident="", label="")
    height.classified_as = type_pattern(width_type_id, types)
    height.value = data["height"]
    height.unit = MeasurementUnit(
        label="Centimetres", id="http://vocab.getty.edu/aat/300379098")

    hmo.dimension = width
    hmo.dimension = height

    return hmo


def creation_pattern(data, types, ):

    # production
    production = Production(ident="", label="")

    data_prod = data["used"]["produced_by_event"]

    # production timespan
    timespan = TimeSpan(ident="", label="")

    timespan.begin_of_the_begin = data_prod["begin"]
    timespan.end_of_the_end = data_prod["end"]

    name = Name(ident="", label="")

    name.content = data_prod["display_title"]
    name.classified_as = type_pattern( "http://vocab.getty.edu/aat/300404669", types)
    timespan.identified_by = name

    production.timespan = timespan

    # production location
    for place in data_prod["location"]:
        production.took_place_at = Place(ident=place["id"], label=place["_label"])

    # production carried out by
    for person in data_prod["person"]:
        production.carried_out_by = Person(ident=person["id"], label=person["_label"])

    # negative
    negative = negative_pattern(data["used"], types)
    negative.produced_by = production
    negative.shows = VisualItem(ident="", label=data["used"]["_label"])

    # creation
    creation = Creation(ident="", label=data["_label"])
    creation.used_specific_object = negative

    return creation


def digitally_shows_pattern(data, types):

    label = data["_label"]

    visual_item = VisualItem(ident="", label=label)
    visual_item.represents_instance_of_type = type_pattern(data["type_id"], types)

    return visual_item


def name_pattern(data, types):

    label = data["_label"]
    name = Name(ident="", label="")
    name.classified_as = type_pattern("http://vocab.getty.edu/aat/300404670", types)
    name.language = Language(ident=data["language"]["id"], label=data["language"]["_label"])

    return name


def identifier_pattern(data, types):
    value = data["value"]
    type_id = data["type"]["id"]
    type_label = data["type"]["_label"]

    identifier = Identifier(content=value, ident="")
    identifier.classified_as = type_pattern(type_id, types)

    return identifier

def digital_service_pattern(data, types):

    digital_service = DigitalService(label="IIIF Image API", ident="")
    digital_service.format = "application/ld+json"
    digital_service.access_point = DigitalObject(ident=data["iiif_image_api"])
    digital_service.conforms_to = InformationObject(ident="http://iiif.io/api/image/3/context.json")

    return digital_service





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