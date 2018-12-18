#!/usr/bin/env bash
n_procs=$(seq 1 4)
IFS=$'\r\n' GLOBIGNORE='*' command eval  'f_names=($(cat functions_list.txt))'
#f_names=$(cat functions_list.txt)
f_len=${#f_names[*]}

j=0

# run processes and store pids in array
for i in $n_procs; do
    if [ $j -lt $f_len ]; then
        let j++
    else
        j=0
    fi
    ./script.sh ${f_names[${i}]} &
    pids[${i}]=$!
done

# wait for all pids
for pid in ${pids[*]}; do
    wait $pid
done
