
# What your project does

This project repository contains files that demonstrate a workflow for transforming Cultural Heritage collections data to Linked Art.

The workflow includes reusable elements so that it can be repurposed with a different data source and/or different data model entities.

The Python code makes use of jsonnet code templates and cromulent Python library.

The code transformed three types of entity to Linked Art:
- digital object i.e. digital image
- humanmadeobject  i.e. photograph negative
- set - photographic collection

# How to install
Clone the GitHub repository .

```git clone https://github.com/tgra/Linked-Art-Collection-Data-Workflow.git```

or download the zip file provided:

https://github.com/tgra/Linked-Art-Collection-Data-Workflow/archive/refs/heads/main.zip

# Example usage

The transform collection data for digital images data, available via the PIA JSON API, to Linked Art:

1. extract data (and save locally)

        ```cd digitalobjevt
        python3 a_query_api.py```

2. map data (to intermediate data template)

        ```python3 b_map_data.py```

3. transform data (to Linked Art)

       ```python3 c_linked_art.py```

# How to set up the dev environment
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
Install the following Python libraries with following pattern:
```python3 -m pip install <name> e.g. python3 -m pip install cromulent```

- cromulent
- requests
- json
- pathlib
- os
- jsonnet
- pyld
  


# How to contribute
To contribute, fork the repository and create a pull request. 

# Change log

# License and authorship information
The code has been written by Tanya Gray @tgra at the University of Oxford. The work is further to a collaboration with Julien Remy at the University of Basel (https://www.unibas.ch/), Tanya Gray and Dr Kevin Page at the University of Oxford as part of the Linked Art II project.


# Further documentation
See [./docs](documentation)

# Bug reporting
Raise an issue via https://github.com/tgra/Linked-Art-Collection-Data-Workflow/issues

# Acknowledgements
This work was undertaken by the Linked Art II project at the University of Oxford (Principal Investigator: Dr. Kevin Page, Oxford e-Research Centre) funded by the UK Arts and Humanities Research Council (AHRC project reference AH/T013117/1). The project's Research Software Engineer was Tanya Gray. We gratefully acknowledge the participation and contributions of our project partners and the wider Linked Art community.

