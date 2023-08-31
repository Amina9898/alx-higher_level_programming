#!/usr/bin/bash
#script that prints the size of the body of the response to a URL request

if [ $# -ne 1 ]; then
    exit 1
fi

url="$1"
response=$(curl -sI "$url")

content_length=$(echo "$response" | awk -F': ''/Content-Length/{print $2}' |tr -d '/r')
echo $content_length
