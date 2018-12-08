# !/bin/bash

if [ "$1" = "clean" ]; then
    printf "Cleaning . . . \n"
    for dir in ./*/
    do
        cd ${dir}
        make clean
        cd ..
    done
    printf "\nDONE\n"
    exit
fi


for dir in ./*/
do
    cd ${dir}
    printf "%s:\n" "${dir}"
    make
    printf "\n"
    if [ $? != 0 ]; then
        printf "\nMake target failed for: %s\n\n" "${dir}"
        exit
    fi
    cd ..
done

printf "\nAll directories successfully built\n"
