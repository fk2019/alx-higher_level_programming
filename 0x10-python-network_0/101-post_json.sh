#!/bin/bash
# psot json data and display response body
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
