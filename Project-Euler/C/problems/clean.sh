#!/bin/bash

for dir in ./*/;
do
    printf "\n%s\n" "$dir"
    cd $dir
    make clean
    cd ..
done;
