#!/bin/bash
# curl body and display size
curl -sI 0:80 | grep "Content-Length" | cut -d' '  -f2
