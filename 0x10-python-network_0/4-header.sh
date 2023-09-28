#!/bin/bash
# script that takes url as an argument sends GET request to the URL & display response
curl -sH "X-School-User-Id: 98" "$1"
