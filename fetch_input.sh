#!/bin/bash

source .sessionkey
curl -b session=${sessionkey} https://adventofcode.com/2020/day/$1/input > day${1}.in || exit
cat day${1}.in