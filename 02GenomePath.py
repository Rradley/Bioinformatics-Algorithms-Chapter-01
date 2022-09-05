#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 18:49:56 2022

@author: radleyrp
"""
file = "../datasets/dataset_746263_3.txt"

def read_file(file_name):
    with open(file_name, "r") as file:
        string = file.read().split()
        file.close()
    return string

def genome(sequences):
    string = sequences[0]
    for i in range(1, len(sequences)):
        string += sequences[i][-1]
    return string

text = read_file(file)
print(text)
output=genome(text)

f = open("answer.txt", "w")
f.write(output)
f.close()
