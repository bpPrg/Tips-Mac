#!/bin/bash
label=7
start=$PWD
while IFS= read -d '' -r dir; do
    osascript -e "tell application \"Finder\" to set label index of alias POSIX file \"$dir\" to $label" > /dev/null
    echo "Applied label to $dir"
done < <(find $start -mindepth 1 -type d -empty -print0)
