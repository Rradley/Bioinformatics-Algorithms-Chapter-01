#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 20:54:38 2022

@author: radleyrp
"""
file = "../datasets/dataset_746263_10.txt"

def read_file(file_name):
    with open(file_name, "r") as file:
        string = file.read().split(' ')
        file.close()
    return string


def overlap(patterns):
    patterns = patterns.split(' ')
    #print(patterns)
    result = {}
    
    for i in range(len(patterns)):
        for j in range(len(patterns)):
            if i != j and patterns[i][1:] == patterns[j][:-1]:
                if patterns[i] not in result.keys():
                    result[patterns[i]] = str(patterns[j])
                elif patterns[j] not in result.values():
                    result[patterns[i]] += ' ' + patterns[j]
    return result
            
 
text = read_file(file)
#text = "AAG AGA ATT CTA CTC GAT TAC TCT TCT TTC"
output= overlap(text)
f = open("answer.txt", "w")
#print(output)
for key in (output.keys()):
    print(key + ': ' + output[key])
    f.write(key + ': ' + output[key]+'\n')
f.close()
