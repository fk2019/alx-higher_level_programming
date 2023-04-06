#!/bin/bash
# respond with custom message in response body
curl -sw "You got me!" 0.0.0.0:5000/catch_me -o /dev/null
