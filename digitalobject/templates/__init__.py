import json
import re
import sys
import os
import collections.abc

class JsonTemplates:

#-----------------------------------------------------------------------
 def __init__(self): 
  self.__template = None
  self.__var_regex = re.compile("\{\{\ [a-zA-Z0-9_]+\ \}\}")
  self.__arr_regex = re.compile("\{\%\ [a-zA-Z0-9_]+\ \%\}")
  self.__cln_regex = re.compile("[a-zA-Z0-9_]+")
  self.__version__ = "0.1.1"

#-----------------------------------------------------------------------
 def is_dict(self,obj):
  return isinstance(obj,collections.abc.Mapping)
   
#-----------------------------------------------------------------------
 def is_iterable(self,obj):
  try:
   iter(obj)
   return True
  except:
   return False

#-----------------------------------------------------------------------
 def clean_key(self,key):
  mtch = self.__cln_regex.search(key)
  if mtch is None:
   return (False,"{} is not valid!".format(key))
  else:
   return (True,mtch.group(0))

#-----------------------------------------------------------------------
 def loads(self,json_str):
  try:
   self.__template = json.loads(json_str)
  except Exception as ex:
   return (False, "Unable to parse json! {}".format(ex))

  return (True,self.__template)

#-----------------------------------------------------------------------
 def load(self,json_path):
  if os.path.isfile(json_path) and json_path.lower().endswith("json"):
   try:
    with open(json_path) as json_in:
     self.__template = json.load(json_in)
   except Exception as ex:
    return (False, "Unable to parse json! {}".format(ex))
  else:
   return (False, "{} is not JSON file")
  return (True,self.__template)
 
#-----------------------------------------------------------------------
 def __evalulate_value(self,value,replace_dict):
  not_found_error = "{} not found in replacement dictionary {}"
  if self.__var_regex.fullmatch(str(value)):
   replace_key = self.clean_key(value)
   if not replace_key[0]:
    return (False,False,replace_key[1])
   replace_key = replace_key[1]
   if replace_key in replace_dict:
    return (True,True,replace_dict[replace_key])
   else:
    return (False,False,not_found_error.format(replace_key,replace_dict))
  elif self.__arr_regex.fullmatch(str(value)):
   replace_key = self.clean_key(value)
   if not replace_key[0]:
    return (False,False,replace_key[1])
   replace_key = replace_key[1]
   
   if replace_key in replace_dict:
    if self.is_iterable(replace_dict[replace_key]):
     return (True,True,replace_dict[replace_key])
    else:
     return (False,False,"{} value must be iterable".format(replace_key))
   else:

    return (False,False,not_found_error.format(replace_key,replace_dict))
   
  else:
   return (True,False,value)
   
#-----------------------------------------------------------------------
 def __scan_nodes(self,nodes,replace_dict):
  for k,v in nodes.items():
   if self.is_dict(v):
    nodes[k] = self.__scan_nodes(v,replace_dict)
   else:
    replace_result = self.__evalulate_value(v,replace_dict)
    if replace_result[0]:
     nodes[k] = replace_result[2]
    else:
     raise Exception("Unable to find a replacement value for '{}. {}'".format(k,replace_result[2]))
  return nodes
  
#-----------------------------------------------------------------------
 def generate(self,replace_dict):

  try:
   result = self.__scan_nodes(dict(self.__template),replace_dict)
  except Exception as ex:
   return (False,"Error: {}".format(ex))
  return (True,result)
