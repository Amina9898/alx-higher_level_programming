#!/bin/bash
# script that prints the size of the body of the response to a URL request
curl -s "$1" | wc -c
