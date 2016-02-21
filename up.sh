#!/bin/bash

com="$1"

git add *
git commit -m '"$com"'
git push -u origin master
