
This repository contains files that demonstrate a workflow for transforming cultural heritage collections data to Linked Art.


# Requirements
To run the Python scripts it's recommended that you create a virtual environment with venv, and install the dependencies listed.

## Install pip

###  macosx  
https://pip.pypa.io/en/stable/installation/
python -m ensurepip --upgrade

## Create virtual environment with venv
https://packaging.python.org/en/latest/tutorials/installing-packages/#creating-virtual-environments
python3 -m venv <DIR>
source <DIR>/bin/activate

## command line install Python libraries

- cromulent
- requests
- json
- pathlib
- os
- jsonnet
- pyld
  
Install the above list, following pattern:
python3 -m pip install <name> e.g. python3 -m pip install cromulent


# Issues encountered with cromulent

## current_owner
cromulent does not support use of this property with digitalobject