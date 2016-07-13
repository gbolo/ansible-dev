#!/usr/bin/env python2

from __future__ import print_function
from powerdns_api import pdns
import yaml
import json

# read config file
with open('infoblox_config.yml', 'r') as f:
    creds = yaml.load(f)

pdnstest = pdns.PowerDNS(creds["powerdns"]["url"], creds["powerdns"]["api_key"])
zones = pdnstest.list_zones()
print(json.dumps(zones))
