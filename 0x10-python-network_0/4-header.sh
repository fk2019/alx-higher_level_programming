#!/bin/bash
# send GET request with custom header
curl -sHX GET "X-School-User-Id=98" "$1"
