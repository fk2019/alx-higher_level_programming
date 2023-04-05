#!/bin/bash
# send GET request with custom header
curl -sXH GET "X-School-User-Id=98" "$1"
