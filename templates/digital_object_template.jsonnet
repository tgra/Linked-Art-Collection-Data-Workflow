local object_title        = std.extVar('title');
local object_id           = std.extVar('id');
local collection_label    = std.extVar('base_path');
local homepage_label      =  'SGV Homepage for PIA ID ' + object_id + (if object_title != '' then ' - ' + object_title else '');
local negative_label      = 'Negative of ' + (if object_title != '' then object_title else object_id);

local production_date_start = std.extVar('date_start');
local production_date_end   = std.extVar('date_end');
local production_date_display = std.extVar('date_display');

local id_place            = std.extVar('place_id');
local id_geonames         = std.extVar('geonames_id');
local label_place         = std.extVar('place_label');

local id_local            = std.extVar('oldnr');
local id_sgv              = std.extVar('signature');

local label_shows         = 'Visual Content of Negative of ' +  (if object_title != '' then object_title else object_id);
local label_digitally_shows = 'Visual Content of Digital Positive of ' +  (if object_title != '' then object_title else object_id);

local base_path           = std.extVar('base_path');
local uri_image_fullres   = "https://sipi.participatory-archives.ch/" + base_path + "/" + id_sgv + '.jp2/full/max/0/default.jpg';

local iiif_label          = 'IIIF Manifest for PIA ID ' + object_id + (if object_title != '' then ' - ' + object_title else '');
local iiif_uri            = 'https://iiif.participatory-archives.ch/' + object_id + '/manifest.json';
local iiif_image_api      = "https://sipi.participatory-archives.ch/" + base_path + "/" + id_sgv + '.jp2/info.json';


{
  id: object_id,
  _label: object_title,
  type: 'http://vocab.getty.edu/aat/300215302',

  member_of: [{
    id: '',
    _label: collection_label,
    type: 'collection',
  }],
  subject_of: [
    {
      type: 'http://vocab.getty.edu/aat/300264578',
      _label: homepage_label,
      access_point_id: '',
    },
    {
      type: 'iiif',
      _label: iiif_label,
      access_point_id: iiif_uri,
    },
  ],
  current_owner: {
    id: 'https://linkedart.participatory-archives.ch/group/42',
    _label: 'SGV Fotoarchiv',
    type_id: 'http://vocab.getty.edu/aat/300343368',
    type_label: 'Photo Archives',
  },

  created_by: {
    _label: 'Digitisation of Photograph',
    used: {
      _label: negative_label,
      width: '',
      height: '',

      produced_by_event: {
        begin: production_date_start,
        end: production_date_end,
        display_title: production_date_display,
        location: [{
          id: id_place,
          geonames_id: id_geonames,
          _label: label_place,
        }],
        person: [{
          id: '',
          _label: '',
        }],

      },
      shows: {

        _label: label_shows,
      },
    },
  },

  identified_by: {

    names: [
      {
        _label: object_title,
        type: {
          id: 'http://vocab.getty.edu/aat/300404670',
          _label: 'Owner-Assigned Title',
        },
        language: {
          id: 'http://vocab.getty.edu/aat/300388344',
          _label: 'German',
        },
      },
    ],
    identifiers: [
      {
        value: id_local,
        type: {
          id: 'http://vocab.getty.edu/aat/300417447',
          _label: 'Creator-Assigned Number',
        },
      },
      {
        value: id_sgv,
        type: {
          id: 'http://vocab.getty.edu/aat/300312355',
          _label: 'SGV Signature',
        },
      },
      {
        value: object_id,
        type: {
          id: 'http://vocab.getty.edu/aat/300404621',
          _label: 'PIA ID',
        },
      },
    ],
  },
  access_point: {
    id: uri_image_fullres,
    _label: 'Image in full resolution',
  },
  iiif_image_api: iiif_image_api,

  digitally_shows: {
    _label: label_digitally_shows,
    type_id: '',
    type_label: '',
  },
}
