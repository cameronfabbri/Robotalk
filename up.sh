#!/bin/bash

if [ "$#" == 0 ] ; then
   echo "enter git commit message"
   exit
fi

com="$1"
rm src/*.pyc
rm src/classifier.pickle

git add *
git commit -m '"$com"'
git push -u origin master
