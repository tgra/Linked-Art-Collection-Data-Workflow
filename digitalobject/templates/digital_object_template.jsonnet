{
  id: std.extVar('id'),
  _label: std.extVar('title'),
  type: 'http://vocab.getty.edu/aat/300215302',

  member_of: [{
    id: '',
    _label: std.extVar('base_path'),
    type: 'collection',
  }],
  subject_of: [
    {
      type: 'http://vocab.getty.edu/aat/300264578',
      _label: 'SGV Homepage for PIA ID ' + std.extVar('id') + ' - ' + std.extVar('title'),
      access_point_id: '',
    },
    {
      type: 'iiif',
      _label: 'IIIF Manifest for PIA ID ' + std.extVar('id') + ' - ' + std.extVar('title'),
      access_point_id: 'https://iiif.participatory-archives.ch/' + std.extVar('id') + '/manifest.json',
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
      _label: 'Negative of ' + std.extVar('title'),
      width: '',
      height: '',

      produced_by_event: {
        begin: '',
        end: '',
        display_title: '',
        location: [{
          id: '',
          _label: '',
        }],
        person: [{
          id: '',
          _label: '',
        }],

      },
      shows: {

        _label: 'Visual Content of Negative of ' + std.extVar('title'),
      },
    },
  },

  identified_by: {

    names: [
      {
        _label: std.extVar('title'),
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
        value: std.extVar('oldnr'),
        type: {
          id: 'http://vocab.getty.edu/aat/300417447',
          _label: 'Creator-Assigned Number',
        },
      },
      {
        value: std.extVar('signature'),
        type: {
          id: 'http://vocab.getty.edu/aat/300312355',
          _label: 'SGV Signature',
        },
      },
      {
        value: std.extVar('id'),
        type: {
          id: 'http://vocab.getty.edu/aat/300404621',
          _label: 'PIA ID',
        },
      },
    ],
  },
  access_point: {
    id: "https://sipi.participatory-archives.ch/" + std.extVar('base_path') + "/" + std.extVar('signature') + '.jp2/full/max/0/default.jpg',
    _label: 'Image in full resolution',
  },
  iiif_image_api: "https://sipi.participatory-archives.ch/" + std.extVar('base_path') + "/" + std.extVar('signature') + '.jp2/info.json',

  digitally_shows: {
    _label: 'Visual Content of Digital Positive of ' + std.extVar('title'),
    type_id: '',
    type_label: '',
  },
}
