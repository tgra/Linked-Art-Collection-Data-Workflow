local sipi_uri = 'https://sipi.participatory-archives.ch/';
local iiif_base_uri = 'https://iiif.participatory-archives.ch/';
local la_base_uri = 'https://data.participatory-archives.ch/';
local aat = 'http://vocab.getty.edu/aat/';

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
local shows_label = 'Visual Content of ' +  (if object_title != '' then object_title else object_id);
// image uri and iiif
local base_path = std.extVar('base_path');
local uri_image_fullres = sipi_uri + base_path + '/' + id_sgv + '.jp2/full/max/0/default.jpg';

local iiif_label = 'IIIF Manifest for PIA ID ' + object_id + (if object_title != '' then ' - ' + object_title else '');
local iiif_uri = iiif_base_uri + id_sgv + '/manifest.json';
local iiif_image_api = sipi_uri + base_path + '/' + id_sgv + '.jp2/info.json';

// image dimensions not avaialable at the moment

local width = '';
local height = '';

// collection
local collection_label = std.extVar('base_path');
local collection_id = std.extVar('collection_id');

{
  id: object_id,
  _label: object_title,
  type_id: 300215302,

  [if collection_id != '' then 'member_of' else null]:
    [{
      id: la_base_uri + 'set/' + collection_id,
      type: 'Set',
      _label: collection_label,
      classified_as: [
        {
          type_id: 300025976
        },
      ],
    }],
  subject_of: [
    {
      type_id: 300264578,
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
    id: la_base_uri + 'group/42',
    _label: 'SGV Fotoarchiv',
    type_id: 300343368,
  },
  [if production_date_start != "" then 'produced_by' else null]: {
        begin: production_date_start,
        end: production_date_end,
        display_title: production_date_display,
        location: [{
          id: id_place,
          geonames_id: id_geonames,
          _label: label_place,
        }],
      },
  shows: {
    _label: shows_label,
  },
   identified_by: {
    [if object_title != '' then 'name' else null]: {
      _label: object_title,
      type_id: 300404670,
      language: {
        type_id: 300388344
      },
    },
    [if id_oldnr != '' then 'creator-assigned' else null]: {
      value: id_oldnr,
      type_id: 300417447,
    },
    [if id_sgv != '' then 'sgv-signature' else null]: {
      value: id_sgv,
      type_id: 300312355,
    },
    [if object_id != '' then 'pia-id' else null]:
      {
        value: object_id,
        type_id: 300404621,
      },
  },
  representation: [{
    digital_surrogate : {
        id: uri_image_fullres,
      _label: 'Digital Surrogate of ' + object_id + ' - ' + object_title,
    },
    iiif_image_api:{
      id: iiif_image_api
    },
  }
  ],
}



    
  