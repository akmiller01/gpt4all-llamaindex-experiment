#!/bin/bash

BASENAME=$(basename -- "$1")
cp "$1" "./data/$BASENAME"
cd ./data
split --additional-suffix="$BASENAME" -l $2 "./$BASENAME" 0
for I in $(seq 1 $(($2 - 1)))
do
    sed -i '1d' "./$BASENAME"
    split --additional-suffix="$BASENAME" -l $2 "./$BASENAME" $I
done
rm ./$BASENAME
cd -