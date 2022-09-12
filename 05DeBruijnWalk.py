#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 20:36:33 2022

@author: radleyrp
"""
file = "../datasets/dataset_746265_8.txt"

def getSuffix(text):
    return text[1:len(text)]

def getPrefix(text):
    return text[0:len(text)-1]

def debruijn(kmers):
  result = {}
  for kmer in kmers:
    if getPrefix(kmer) not in result:
      result[getPrefix(kmer)] = getSuffix(kmer)
    else:
      result[getPrefix(kmer)] += ' ' + getSuffix(kmer)
  return result


def read_file(file_name):
    with open(file_name, "r") as file:
        text = file.readline().split()
        file.close()
    return text

kmers = read_file(file)
result = debruijn(kmers)
print(result)

for key in sorted(result.keys()):
    print(key + ': ' + result[key])
    