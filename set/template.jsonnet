local iiif_base_uri = 'https://iiif.participatory-archives.ch/';
local la_base_uri = 'https://linkedart.participatory-archives.ch/';
local aat = 'http://vocab.getty.edu/aat/';
local salsah_uri = "https://archiv.sgv-sstp.ch/";

// title and id
local set_label = std.extVar('label');
local set_id = std.extVar('id');

// identifiers
local id_pia = set_id;
local id_sgv = std.extVar('signature');


// homepage label
local homepage_label = 'SGV Homepage for ' + set_label;
local homepage_uri = salsah_uri + 'collection/' +  id_sgv + '/';

// iiif
local iiif_label = 'IIIF Collection for  ' + set_label;
local iiif_uri = iiif_base_uri + 'collections/' + set_id + '.json';

// description
local description = std.extVar('description');


{
  id: la_base_uri + 'set/' + set_id,
  _label: set_label,
  type_id: 300025976,

  
  
  subject_of: 
    [{
    [if id_sgv != '' then 'homepage' else null]: 
        {
      type_id: 300264578,
      _label: homepage_label,
      access_point_id: homepage_uri,
        }
    ,
    [if iiif_uri != '' then 'iiif' else null]: 
    {
      type: 'iiif',
      _label: iiif_label,
      access_point_id: iiif_uri,
    }
    }],
  
    identified_by: {
    [if set_label != '' then 'name' else null]: {
      _label: set_label,
      type_id: 300404670,
      language: {
        type_id: 300388344
      },
    },
    
    [if id_sgv != '' then 'sgv-signature' else null]: {
      value: id_sgv,
      type_id: 300312355,
    },
    [if set_id != '' then 'pia-id' else null]:
      {
        value: set_id,
        type_id: 300404621,
      },
  },
  
[if description != '' then 'description' else null]:
   description
  
}



    
  