#!/usr/bin/env python2

import subprocess
import json
import sys
import os

cmd_env = os.environ.copy()
cmd_env["GOPATH"] = '/opt/gopath'
cmd_env["PATH"] = '$GOPATH/bin:$PATH' + cmd_env["PATH"]
cmd = ['/opt/gopath/bin/peer', 'network', 'list']
cluster_size = 4
quarum = cluster_size / 2 + 1

try:
  pipe = subprocess.Popen(cmd, env=cmd_env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  stdout, stderr = pipe.communicate()
  returncode = pipe.returncode
  if returncode == 0:
      vp_nodes_dict = json.loads(stdout)
      node_count = len(vp_nodes_dict["peers"]) + 1
      node_ratio = str(node_count) + "/" + str(cluster_size)
      if node_count == cluster_size:
          print "OK: " + node_ratio + " ALL Fabric Validating Peers are Alive"
          sys.exit(0)
      elif node_count >= quarum:
          print "WARN: " + node_ratio + " Some Fabric Validating Peers are Down. QUARUM is OK."
          sys.exit(1)
      else:
          print "CRITICAL: " + node_ratio + " QUARUM HAS BEEN LOST!"
          sys.exit(2)
  else:
      print "CRITICAL: Peer returned non-zero response code"
      sys.exit(2)
except Exception as e:
  print(e)
  sys.exit(2)
