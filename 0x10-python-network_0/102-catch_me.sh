#!/bin/bash
# respond with custom message in response body
message="You got me!"
curl -sw "$message" 0.0.0.0:5000/catch_me -o /dev/null
