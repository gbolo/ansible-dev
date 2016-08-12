#!/usr/bin/env python2

from docker import Client
import sys

cli = Client(base_url='unix://var/run/docker.sock')

docker_filters = {}
docker_filters['ancestor'] = 'hyperledger/fabric-baseimage'
docker_filters['status'] = 'running'

try:
  chaincode_containers = len(cli.containers(filters=docker_filters))
  if chaincode_containers == 0:
    print "CRITICAL: NO CHAINCODE CONTAINERS RUNNING!"
    sys.exit(2)
  else:
    print "OK: " + str(chaincode_containers) + " Chaincode Container(s) Running"
    sys.exit(0)
except Exception as e:
  print "CRITICAL: Cannot connect to docker socket!"
  sys.exit(2)
