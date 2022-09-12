#!/usr/bin/env python3
"""
Created on Thu Sep  8 21:14:03 2022

@author: radleyrp
"""
import networkx as nx

file = '../datasets/dataset_746269_16.txt'

with open (file, 'r') as f:
  inputLines = f.read().splitlines()
k, d = inputLines[0].split(' ')
k, d = int(k), int(d)
patterns = inputLines[1].split(' ')

"""
def getSuffix(text,k):
    #return text[1:len(text)]
    return text[1:k] + text[k] + text[k+2:]

def getPrefix(text,k):
    #return text[0:len(text)-1]
    return text[0:k-1] + text[k] + text[k+1:2*k]

def debruijn(kmers,k):
  result = {}
  for kmer in kmers:
    if getPrefix(kmer,k) not in result:
      result[getPrefix(kmer,k)] = getSuffix(kmer,k)
    else:
      result[getPrefix(kmer,k)] += ' ' + getSuffix(kmer,k)
  return result
"""
def debruijn(kmers, k):
    graph = {}   
    for kmer in kmers:
        prefix = kmer[0:k-1] + kmer[k] + kmer[k+1:2*k]
        suffix = kmer[1:k] + kmer[k] + kmer[k+2:]
        graph[prefix] = [suffix]
    return graph
l = len(debruijn(patterns, k))
graph = nx.DiGraph(debruijn(patterns, k))


def eulerianPath(graph):
    nodes = list(graph.nbunch_iter())
    for node in nodes:
        if graph.in_degree(node) < graph.out_degree(node):
           print(node, graph.in_degree(node), graph.out_degree(node))
           path = list(nx.dfs_edges(graph, node))
           break
    text = path[0][0][:k-1]
    for i in range (0, len(path)):
        text += path[i][1][k-2]
    for j in range(l-k-d, len(path)):
        text += path[j][1][-1]
    print(text)

eulerianPath(graph)