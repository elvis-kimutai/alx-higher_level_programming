#!/bin/bash
#script that sends delete request to the URL passed as the first argument & displays body of response
curl -sX DELETE "$1"
