#!/bin/bash                                                                     
tr -cs '[:graph:]' '[\n*]' | sort -u | comm -23 - sorted.words

#changed it form A-Za-z to [:graph:]
							#^^^^ all character or smt
							
