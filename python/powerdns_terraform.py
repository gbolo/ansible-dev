#!/usr/bin/env python2

from __future__ import print_function
from powerdns_api import pdns
import yaml
import json

# Config options
create_ptr = True

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

        # append A record
        tf_json['resource']['powerdns_record'][res_name] = {}
        tf_json['resource']['powerdns_record'][res_name]['type'] = "A"
        tf_json['resource']['powerdns_record'][res_name]['ttl'] = "300"
        tf_json['resource']['powerdns_record'][res_name]['name'] = hostname
        tf_json['resource']['powerdns_record'][res_name]['records'] = records
        tf_json['resource']['powerdns_record'][res_name]['zone'] = zone

        # append PTR record if starts with 10.x
        res_name_ptr = res_name + "_ptr"
        zone_ptr = "10.in-addr.arpa"
        records_ptr = []
        records_ptr.append(hostname)
        ip = creds["records"]["host"][hostname]
        name_ptr = '.'.join( ip.split('.')[-1:0:-1] ) + "." + zone_ptr

        tf_json['resource']['powerdns_record'][res_name_ptr] = {}
        tf_json['resource']['powerdns_record'][res_name_ptr]['type'] = "PTR"
        tf_json['resource']['powerdns_record'][res_name_ptr]['ttl'] = "3600"
        tf_json['resource']['powerdns_record'][res_name_ptr]['name'] = name_ptr
        tf_json['resource']['powerdns_record'][res_name_ptr]['records'] = records_ptr
        tf_json['resource']['powerdns_record'][res_name_ptr]['zone'] = zone_ptr

    except Exception as e:
        print(e)

# output tf.json
print( json.dumps(tf_json) )
