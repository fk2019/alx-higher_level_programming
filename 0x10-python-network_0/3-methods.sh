#!/bin/bash
# Display all HTTP methods served by server
curl -sI "$1" | grep "Allow" | cut -d' ' -f2
