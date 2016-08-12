#!/bin/bash
# gbolo
# Quick check for ntp offset of external ntp server

WARNING=0
CRITICAL=2
CMD="/usr/bin/who"
CMD_OUTPUT=$($CMD 2>&1)
SSH_USERS=$(echo $CMD_OUTPUT | grep -v localhost | grep -v -e '^$' | wc -l)

if [ $? -ne 0 ]
then
  echo "UNKNOWN: error executing $CMD"
  exit 2
fi

if (( $SSH_USERS > $CRITICAL ));
then
  echo "CRITCAL: $SSH_USERS users connected via ssh: $CMD_OUTPUT"
  exit 2
elif (( $SSH_USERS > $WARNING ));
then
  echo "WARNING: $SSH_USERS users connected via ssh: $CMD_OUTPUT"
  exit 1
else
  echo "OK: nobody connected via ssh"
  exit 0
fi
