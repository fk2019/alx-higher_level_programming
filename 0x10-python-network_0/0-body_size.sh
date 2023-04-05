#!/bin/bash
# curl body and display size
curl -sI "$1" | grep "Content-Length" | cut -d' '  -f2
