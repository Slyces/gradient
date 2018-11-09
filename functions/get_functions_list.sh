# !/usr/bin/env/bash

# download the list
if [ ! -f functions_list.txt ]; then
    wget -q -O - https://www.sfu.ca/~ssurjano/Code/ | grep -iP '\"[\w\d]+?m\.html\"' | sed -E 's/^.*\"(.*?)m\.html\".*$/\1/' > functions_list.txt
fi
# get only the matlab
