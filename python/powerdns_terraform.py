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

def add_record(res_name, record_type, ttl, name, record, zone):
    global tf_json
    if res_name in tf_json['resource']['powerdns_record']:
        tf_json['resource']['powerdns_record'][res_name]['records'].append(record)
    else:
        tf_json['resource']['powerdns_record'][res_name] = {}
        tf_json['resource']['powerdns_record'][res_name]['type'] = record_type
        tf_json['resource']['powerdns_record'][res_name]['ttl'] = ttl
        tf_json['resource']['powerdns_record'][res_name]['name'] = name
        tf_json['resource']['powerdns_record'][res_name]['records'] = []
        tf_json['resource']['powerdns_record'][res_name]['records'].append(record)
        tf_json['resource']['powerdns_record'][res_name]['zone'] = zone

# generate tf json
for hostname in creds["records"]["host"]:
    try:
        res_name = hostname.replace(".", "_")
        res_name = res_name.replace("*", "wildcard")
        zone = '.'.join( hostname.split('.')[1:] )
        ip = creds["records"]["host"][hostname]
        # append A record
        add_record(res_name, "A", "300", hostname, ip, zone)

        # append PTR record if starts with 10.x and boolean set and no wildcard
        if ip.startswith("10.") and create_ptr and not hostname.startswith("*"):
            res_name_ptr = ip + "_ptr"
            res_name_ptr = res_name_ptr.replace(".", "_")
            zone_ptr = "10.in-addr.arpa"
            name_ptr = '.'.join( ip.split('.')[-1:0:-1] ) + "." + zone_ptr
            # append ptr record
            add_record(res_name_ptr, "PTR", "3600", name_ptr, hostname, zone_ptr)

    except Exception as e:
        print(e)

# output tf.json
print( json.dumps(tf_json) )
