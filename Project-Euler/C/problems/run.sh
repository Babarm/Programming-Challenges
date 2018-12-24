#!/bin/bash

./make.sh

for dir in ./*/;
do
    $dir/a.out
done;
