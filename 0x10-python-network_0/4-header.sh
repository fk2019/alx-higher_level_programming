#!/bin/bash
# send GET request with custom header
curl "$1"  -sX -H GET "X-School-User-Id=98"
