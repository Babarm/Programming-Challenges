#!/bin/bash

for i in {001..650};
do
    cd Problem-$i
    printf "\nProblem $i:\n"
    make clean
    cd ..
done
