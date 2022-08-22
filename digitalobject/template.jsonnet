local sipi_uri = 'https://sipi.participatory-archives.ch/';
local iiif_base_uri = 'https://iiif.participatory-archives.ch/';
local la_base_uri = 'https://linkedart.participatory-archives.ch/';
local aat = 'http://vocab.getty.edu/aat/';
local salsah_uri = "https://archiv.sgv-sstp.ch/";
// title and id
local object_title = std.extVar('title');
local object_id = std.extVar('id');


// labels

local homepage_label = 'SGV Homepage for PIA ID ' + object_id + (if object_title != '' then ' - ' + object_title else '');
local negative_label = 'Negative of ' + (if object_title != '' then object_title else object_id);

// production date
local production_date_start = std.extVar('date_start');
local production_date_end = std.extVar('date_end');
local production_date_display = std.extVar('date_display');

// production place
local id_place = std.extVar('place_id');
local id_geonames = std.extVar('geonames_id');
local label_place = std.extVar('place_label');


// production person not available at moment

local production_person_id = '';
local production_person_label = '';

// identifiers
local id_oldnr = std.extVar('oldnr');
local id_sgv = std.extVar('signature');
local salsah_id = std.extVar("salsah_id");

// shows
local label_shows = 'Visual Content of Negative of ' + (if object_title != '' then object_title else object_id);

// digitally shows
local label_digitally_shows = 'Visual Content of Digital Positive of ' + (if object_title != '' then object_title else object_id);


// image uri and iiif
local base_path = std.extVar('base_path');
local uri_image_fullres = sipi_uri + base_path + '/' + id_sgv + '.jp2/full/max/0/default.jpg';

local iiif_label = 'IIIF Manifest for PIA ID ' + object_id + (if object_title != '' then ' - ' + object_title else '');
local iiif_uri = iiif_base_uri + object_id + '/manifest.json';
local iiif_image_api = sipi_uri + base_path + '/' + id_sgv + '.jp2/info.json';


// image dimensions not avaialable at the moment

local width = '';
local height = '';

// collection
local collection_label = std.extVar('base_path');
local collection_id = std.extVar('collection_id');


//=================================

// template

{
  id: object_id,
  _label: object_title,
  type: aat + '300215302',

  [if collection_id != '' then 'member_of' else null]:
    [{
      id: la_base_uri + 'set/' + collection_id,
      type: 'Set',
      _label: collection_label,
      classified_as: [
        {
          id: aat + '300025976',
          type: 'Type',
          _label: 'Collection',
        },
      ],
    }],

  subject_of: [
    {
      type: aat + '300264578',
      _label: homepage_label,
      access_point_id: salsah_uri + 'resource/' + salsah_id,
    },
    {
      type: 'iiif',
      _label: iiif_label,
      access_point_id: iiif_uri,
    },
  ],
  current_owner: {
    id: la_base_uri + 'group/42',
    _label: 'SGV Fotoarchiv',
    type_id: aat + '300343368',
    type_label: 'Photo Archives',
  },

  created_by: {
    _label: 'Digitisation of Photograph',
    used: {
      _label: negative_label,

      [if width != '' then 'width' else null]: width,
      [if height != '' then 'height' else null]: height,

      [if production_date_start != '' then 'produced_by_event' else null]:
        {
          begin: production_date_start,
          end: production_date_end,
          display_title: production_date_display,

          [if id_place != '' then 'location' else null]:
            [{
              id: id_place,
              geonames_id: id_geonames,
              _label: label_place,
            }],

          [if production_person_id != '' then 'person' else null]:
            [{
              id: production_person_id,
              _label: production_person_label,
            }],

        },
      [if label_shows != '' then 'shows' else null]:
        {
          _label: label_shows,
        },
    },
  },

  identified_by: {

    [if object_title != '' then 'name' else null]: [{
      _label: object_title,
      type: {
        id: aat + '300404670',
        _label: 'Owner-Assigned Title',
      },
      language: {
        id: aat + '300388344',
        _label: 'German',
      },
    }],

    
    [if id_oldnr != '' then 'creator-assigned' else null]: [{
      value: id_oldnr,
      type: {
        id: aat + '300417447',
        _label: 'Creator-Assigned Number',
      },
    }],
    [if id_sgv != '' then 'sgv-signature' else null]: [{
      value: id_sgv,
      type: {
        id: aat + '300312355',
        _label: 'SGV Signature',
      },
    }],

    [if object_id != '' then 'pia-id' else null]:
      [{
        value: object_id,
        type: {
          id: aat + '300404621',
          _label: 'PIA ID',
        },
      }],

  },


  [if uri_image_fullres != '' then 'access_point' else null]:
    {
      id: uri_image_fullres,
      _label: 'Image in full resolution',
    },

  [if iiif_image_api != '' then 'iiif_image_api' else null]: iiif_image_api,

  [if label_digitally_shows != '' then 'digitally_shows' else null]:
    {
      _label: label_digitally_shows,
      //type_id: '',
      // type_label: '',
    },
}
