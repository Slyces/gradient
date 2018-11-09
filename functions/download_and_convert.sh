#!/usr/bin/env bash
func="$1"
wget -q "https://www.sfu.ca/~ssurjano/Code/${func}m.html" -O "${func}.m"
sed -iE '/^<.*$/d' "./${func}.m"
sudo smop "${func}.m" &> /dev/null
rm "${func}.m" "${func}.mE"
