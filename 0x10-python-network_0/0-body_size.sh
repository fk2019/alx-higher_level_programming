#!/bin/bash
# curl body and display size
curl -sI GET 0:80 | grep "Content-Length" | cut -d' '  -f2
