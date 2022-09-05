#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 20:36:33 2022

@author: radleyrp
"""
file = "../datasets/dataset_746265_8.txt"

def read_file(file_name):
    with open(file_name, "r") as file:
        string = [line.strip() for line in file.readlines()]
        file.close()
    return string

def debruijn(patterns):
    result = {}
    for i in patterns:
        if i[:-1] not in result.keys():
            result[i[:-1]] = i[1:]
        else:
            result[i[:-1]] += ','+ i[1:]
        #print(result[i])
    return result

text = read_file(file)
#text= 'GAGG CAGG GGGG GGGA CAGG AGGG GGAG'
output = debruijn(text)


f = open("answer.txt", "w")
for key in sorted(output.keys()):
    print(key + ': ' + output[key])
    f.write(key + ': ' + output[key]+'\n')
f.close()
    