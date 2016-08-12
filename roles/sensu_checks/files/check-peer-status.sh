#!/bin/bash
# gbolo
# Quick check hyperledger peer status
export GOPATH=/opt/gopath
export PATH=$GOPATH/bin:$PATH

CMD="/opt/gopath/bin/peer node status"
CMD_OUTPUT=$($CMD 2>&1)

if [ $? -ne 0 ]
then
  echo "UNKNOWN: error executing $CMD --> $CMD_OUTPUT"
  exit 2
fi

if [ $CMD_OUTPUT == "status:STARTED" ];
then
  echo "OK: Peer status is STARTED"
  exit 0
else
  echo "CRITICAL: $CMD_OUTPUT"
  exit 2
fi
