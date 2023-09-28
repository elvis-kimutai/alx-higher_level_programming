#!/bin/bash
#script takes in a url and displays HTTP methods the server will accept
curl -sI "$1" | grep "Allow:" | cut -d " " -f2-
