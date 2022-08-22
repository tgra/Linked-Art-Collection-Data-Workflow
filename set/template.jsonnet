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
  type: aat + '300025976',

  
  
  subject_of: 
    [{
    [if id_sgv != '' then 'homepage' else null]: 
        {
      type: aat + '300264578',
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
    [if set_label != '' then 'name' else null]: [{
      _label: set_label,
    }],

    
    [if id_sgv != '' then 'sgv-signature' else null]: [{
      value: id_sgv,
      type: {
        id: aat + '300312355',
        _label: 'SGV Signature',
      },
    }],

    [if set_id != '' then 'pia-id' else null]:
      [{
        value: set_id,
        type: {
          id: aat + '300404621',
          _label: 'PIA ID',
        },
      }],

  },

[if description != '' then 'description' else null]:
   description
  
}



    
  