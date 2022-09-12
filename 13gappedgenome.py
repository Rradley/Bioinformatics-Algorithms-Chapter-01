#!/usr/bin/env python3
"""
Created on Fri Sep  9 20:26:17 2022

@author: radleyrp
"""

file = '../datasets/dataset_746273_4.txt'
file = '../datasets/dataset_746269_16.txt'

def gappedGenome(patterns, k, d):
  prefix = suffix = ''
  
  for i, patt in enumerate(patterns):
    if i != len(patterns)-1:
      prefix += patt[0][0]
      suffix += patt[1][0]
    else:
      prefix += patt[0]
      suffix += patt[1]
  
  for i in range(k+d+1, len(prefix)):
    if prefix[i] != suffix[i-k-d-1]:
      return "There is no string spelled by the gapped patterns"
  return prefix + suffix[len(suffix)-k-d-1: ]

k = 50
d = 200
with open (file, 'r') as f:
  inputLines = f.read().splitlines()
k, d = inputLines[0].split(' ')
k, d = int(k), int(d)
patterns = inputLines[1].split(' ')

#k = 4
#d = 20
#inputLines = ['GACC|GCGC', 'ACCG|CGCC', 'CCGA|GCCG', 'CGAG|CCGG', 'GAGC|CGGA']

#k = 2
#d = 4
#inputLines = ['GC|CG', 'CA|GT', 'AT|TG', 'TA|GC', 'AC|CA', 'CC|AT']

patterns = []
i = 0
for line in patterns:
  i = i+1
  #print(line.find(' '))
  patterns.append(line.split('|'))
print(gappedGenome(patterns, k-1, d))