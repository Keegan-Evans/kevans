#!/bin/bash

# get target module
target_module_directory=$1
printf "%s\n" "$(target_module_directory)"
printf "Contents of target directory: \n%s\n" ["ls \"$(target_module_directory)\""]
# check for/locate or create target module init
echo "file already added to your __init__"
# parse target and locate functions
# append to init

# stretch goals:
# specify list of things not to add to init
