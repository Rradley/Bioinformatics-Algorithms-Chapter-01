#!/usr/bin/env python3
"""
Created on Fri Sep  9 14:09:38 2022

@author: radleyrp
"""
file = "../datasets/dataset_746263_10.txt"

def getSuffix(string):
    return string[1:len(string)]

def getPrefix(string):
    return string[0:len(string)-1]

def overlapGraph(genome):
  genome.sort()
  for suffix in genome:
    for prefix in genome:
      if getSuffix(suffix) == getPrefix(prefix):
        print(suffix +": "+prefix)

with open (file, 'r') as f:
    for line in f.readlines():
        inputLines = line.strip().split()
overlapGraph(inputLines)