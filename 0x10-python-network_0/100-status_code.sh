#!/bin/bash
# display status code without using redirections, ; etc
curl -sw "%{response_code}" "$1" -o /dev/null
