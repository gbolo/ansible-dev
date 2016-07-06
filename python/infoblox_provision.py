#!/usr/bin/env python2

from __future__ import print_function
from infoblox_api import infoblox
import yaml

# disable warning for invalid ssl certs
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# read config file
with open('infoblox_config.yml', 'r') as f:
    creds = yaml.load(f)

# create object
iba_api = infoblox.Infoblox(creds["infoblox"]["hostname"],
                            creds["infoblox"]["username"],
                            creds["infoblox"]["password"],
                            creds["infoblox"]["version"],
                            creds["infoblox"]["dns_view"],
                            creds["infoblox"]["network_view"])


# Create HOST records (A/PTR)
print ('CREATING HOST RECORDS')
for hostname in creds["records"]["host"]:
    try:
        ip = iba_api.create_host_record(creds["records"]["host"][hostname], hostname)
        print(hostname + " -> " + ip)
    except Exception as e:
        print(e)

# Create CNAME records
print ('CREATING CNAME RECORDS')
for cname in creds["records"]["cname"]:
    try:
        ip = iba_api.create_cname_record(cname, creds["records"]["cname"][cname])
        print(cname + " -> " + creds["records"]["cname"][cname])
    except Exception as e:
        print(e)
