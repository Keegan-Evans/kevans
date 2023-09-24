#!/usr/bin/env bash
# store and register python functions to personal python library
#cp $1 $pwd/pocket_kit/
my_lib_fp="/Users/keeganevans/repo/kevans/pocket_kit"
cp $1 $my_lib_fp

printf '%s copied to: %s' "$1" "$my_lib_fp"

# no setup and register inpocket_kit....might be unnecessary with proper library setup
