#!/usr/bin/env bash

if [ $# -ne 1 ]; then
    exit 1
fi

url="$1"
response=$(curl -sI "$url")

content_length=$(echo "$response" | awk -F': ''/Content-Length/{print $2}' |tr -d '/r')
echo $content_length
