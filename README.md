
# Introduction

This project repository contains files that demonstrate a workflow for transforming Cultural Heritage collections data to Linked Art.

The workflow includes reusable elements so that it can be repurposed with a different data source and/or different data model entities.

The Python code makes use of jsonnet code templates and cromulent Python library, and transforms three types of photographic entity to their corresponding representation in Linked Art:
- digital photographic image 
  - to digitalobject
- photographic negative 
  - to humanmadeobject
- photographic collection
  -  to set

# How to install

## Clone the GitHub repository
```
    git clone https://github.com/tgra/Linked-Art-Collection-Data-Workflow.git
```

or 

## Download the zip file provided

https://github.com/tgra/Linked-Art-Collection-Data-Workflow/archive/refs/heads/main.zip

# Example usage
There are three main scripts:
- query_api.py - queries the PIA API
- map_data.py - maps collection data to intermediate JSON format
- linked_art.py - transforms intermediate JSON format to Linked Art JSON-LD

To list the required script arguments use <i>-h</i> e.g.:
```python
python query_api.py -h
```

To transform collection data for digital images data, available via the PIA JSON API, to Linked Art:

1. extract data (and save locally)
```python
query_api.py  --config <config-file>
```
e.g.
```python
python3 query_api.py --config ./digitalobject/settings.yaml 
```

2. map data (to intermediate data template)
```python
map_data.py --objtype <objecttype> --config <config-file> --template <jsonnet-template-filepath>
```
e.g.
```python
python3 map_data.py --objtype set --config set/settings.yaml --template set/template.jsonnet
```
3. transform data (to Linked Art)

```python
python3 linked_art.py --objtype <objecttype> --config <config-file> 
```
e.g.
```python
python3 linked_art.py --objtype set --config set/settings.yaml
```





# How to set up the dev environment
To run the Python scripts it's recommended that you create a virtual environment with venv, and install the dependencies listed.

## Install pip

###  macosx  
https://pip.pypa.io/en/stable/installation/

```python
python -m ensurepip --upgrade
```
## Create virtual environment with venv
https://packaging.python.org/en/latest/tutorials/installing-packages/#creating-virtual-environments

```python
python3 -m venv <DIR>
source <DIR>/bin/activate
```

## command line install Python libraries
Install the following Python libraries with following pattern:
```python 
python3 -m pip install <name> 
```
For example: 
```python
python3 -m pip install cromulent getopt json jsonnet os pathlib pyld requests sys  traceback yaml
```

- cromulent
- getopt
- json
- jsonnet
- os
- pathlib
- pyld
- requests
- sys 
- traceback
- yaml



# How to contribute
To contribute, fork the repository and create a pull request. 

# Change log

# License and authorship information
The code has been written by Tanya Gray @tgra at the University of Oxford. The work is further to a collaboration with Julien A. Raemy at the University of Basel's Digital Humanities Lab, Tanya Gray and Dr Kevin Page at the University of Oxford as part of the Linked Art II project.


# Further documentation
See [./docs](documentation)

# Bug reporting
Raise an issue via https://github.com/tgra/Linked-Art-Collection-Data-Workflow/issues

# Acknowledgements
This work was undertaken by the Linked Art II project at the University of Oxford (Principal Investigator: Dr. Kevin Page, Oxford e-Research Centre) funded by the UK Arts and Humanities Research Council (AHRC project reference AH/T013117/1). 

The project's Research Software Engineer was Tanya Gray. 

We gratefully acknowledge the participation and contributions of our project partners and the wider Linked Art community.

