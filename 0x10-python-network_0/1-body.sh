#!/bin/bash
# A script that sends a request to URL and return body of response

if [ $# -ne 1 ]; then
    exit 1
fi

URL="$1"

response=$(curl -s -w "%{http_code}" -o /dev/stdout "$URL")

http_status="${response: -3}"

if [ "$http_status" = "200" ]; then
	body=$(echo "$response" | head -c -3)
	echo "$body"
fi
