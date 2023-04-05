#!/bin/bash
# send GET request with custom header
curl "$1" -sXH GET "X-School-User-Id=98"
