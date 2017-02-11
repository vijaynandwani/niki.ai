#!/bin/sh

for f in $(find ./data -name '*.csv')
do
    egrep '^[789]\d{9}' "$f"
done


    