#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 20:11:52 2022

@author: radleyrp
"""
file = "../datasets/dataset_746264_6.txt"

def composition(text, k):
  kmers = []
  for i in range(len(text)-k+1):
    kmers.append(text[i:i+k])
  return kmers

def getSuffix(string):
    print('suffix',string[1:len(string)])
    return string[1:len(string)]

def getPrefix(string):
    print('prefix',string[0:len(string)-1])
    return string[0:len(string)-1]

def debruijn(genome, k):
  result = {}
  kmers = composition(genome, k)
  for kmer in kmers:
    if getPrefix(kmer) not in result:
      result[getPrefix(kmer)] = getSuffix(kmer)
    else:
      result[getPrefix(kmer)] += ' ' + getSuffix(kmer)
  return result


def read_file(file_name):
    with open(file_name, "r") as file:
        k = int(file.readline().strip())
        string = file.readline().strip()
        file.close()
    return k,string

k, genome = read_file(file)
k=4
genome='ALPHABET'
result = debruijn(genome, k)

for key, value in sorted(result.items()):
  print(key + ": " + value)



#f = open("answer.txt", "w")
#for key in sorted(output.keys()):
#    print(key + ': ' + output[key])
#    f.write(key + ': ' + output[key]+'\n')
#f.close()



