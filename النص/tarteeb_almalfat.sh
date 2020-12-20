#!/usr/bin/bash


from=1
to=20

for file in $( eval echo {$from..$to} )
do
       echo "do something right $file"
done

