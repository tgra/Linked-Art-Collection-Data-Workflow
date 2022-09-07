# Introduction
This 'how-to' file describes how to query the PIA API using the 'query_api.py' file.

The query_api.py file queries the PIA JSON API using the URL provided in a config .yaml file specified in the script argument --config

 An example config file can be viewed at [./digitalobject/settings.yaml](example settings.yaml)


# Files
- query_api.py 
- settings.py - uses function 'query_api()' to check that correct script arguments have been provided


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
