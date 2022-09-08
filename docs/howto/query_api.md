# How to - query the PIA API using the 'query_api.py' file

## Introduction

The query_api.py file queries the PIA JSON API and writes the JSON files returned to a local directory, ready for transformation to Linked Art JSON-LD.

A .yaml file is used for script variables. The filepath for the .yaml file is specified as a script argument --config

## Example settings.yaml  file

A settings.yaml file is specified in the script argument --config. 

An example config file can be viewed at [example settings.yaml](/digitalobject/settings.yaml)

Example content:

```yaml
- - - # settings for digital object
- settings:
  default_lang        : en
  base_url            : https://linkedart.participatory-archives.ch/
  pia_api_uri         : https://data.participatory-archives.ch/api/v1/images
  pia_api_include     : include=collections,date,place
  page_size           : 500
  directory           : digitalobject/
  a_collection        : data/a_collection
  b_mapped            : data/b_mapped
  c_linked_art        : data/c_linked_art
  template            : template.jsonnet
...
```

The query URL for the PIA API query is contstructed using 'pia_api_url' and 'pia_api_include' in the settings.yaml file

JSON files are written to a local directory, with the filepath constructed using the 'directory', 'a_collection' and 'page_size' variables in the setting.yaml file.


## Files
- query_api.py - main script
- settings.py - use function 'query_api()' to check that the correct script arguments have been provided


# Help
The following will provide information about arguments to use with the script.
```
python3 query_api.py -h 
```

# Example command

```python
query_api.py  --config <config-file>
```
e.g.
```python
python3 query_api.py --config ./digitalobject/settings.yaml 
```
