#!/bin/bash
#mak a post request with json file
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
