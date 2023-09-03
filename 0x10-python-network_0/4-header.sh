#!/bin/bash
#script that takes in URL as argument, sends GET request, and displays response
curl -sH "X-School-User-Id: 98" "$1"
