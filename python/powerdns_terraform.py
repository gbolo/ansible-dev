#!/usr/bin/env python2

from __future__ import print_function
from powerdns_api import pdns
import yaml
import json

# read config file
with open('infoblox_config.yml', 'r') as f:
    creds = yaml.load(f)

# Create json terraform object
tf_json = {}
tf_json['provider'] = {}
tf_json['provider']['powerdns'] = {}
tf_json['provider']['powerdns']['server_url'] = creds["powerdns"]["url"]
tf_json['provider']['powerdns']['api_key'] = creds["powerdns"]["api_key"]

tf_json['resource'] = {}
tf_json['resource']['powerdns_record'] = {}

# generate tf json
for hostname in creds["records"]["host"]:
    try:
        res_name = hostname.replace(".", "_")
        zone = '.'.join( hostname.split('.')[1:] )
        records = []
        records.append( creds["records"]["host"][hostname] )
        # append tf_json
        tf_json['resource']['powerdns_record'][res_name] = {}
        tf_json['resource']['powerdns_record'][res_name]['type'] = "A"
        tf_json['resource']['powerdns_record'][res_name]['ttl'] = "300"
        tf_json['resource']['powerdns_record'][res_name]['name'] = hostname
        tf_json['resource']['powerdns_record'][res_name]['records'] = records
        tf_json['resource']['powerdns_record'][res_name]['zone'] = zone
    except Exception as e:
        print(e)

# output tf.json
print( json.dumps(tf_json) )
