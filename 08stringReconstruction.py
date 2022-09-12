#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 17:09:01 2022

@author: radleyrp
"""
from random import choice

file = '../datasets/dataset_746268_7.txt'

def read_file(file_name):
    with open(file_name, "r") as file:
        kmer = file.readline().split()
        text = file.readline().split()
        file.close()
    return kmer, text

def genome(sequences):
    string = sequences[0]
    for i in range(1, len(sequences)):
        string += sequences[i][-1]
    return string

def composition(text, k):
  kmers = []
  k = int(k[0])
  for i in range(len(text)-k+1):
    kmers.append(text[i:i+k])
  return kmers

def getSuffix(text):
    return text[1:len(text)]

def getPrefix(text):
    return text[0:len(text)-1]

def debruijn(kmers):
  result = {}
  for kmer in kmers:
    if getPrefix(kmer) not in result:
      result[getPrefix(kmer)] = [getSuffix(kmer)]
    else:
      result[getPrefix(kmer)] += ' ' + getSuffix(kmer)   
  return result

def removeEdge(graph, startNode, targetNode):
  graph[startNode].remove(targetNode)
  if not graph[startNode]:
    del graph[startNode]
  return graph

def eulerianCycle(graph):
    startNode, edges = choice(list(graph.items()))
    targetNode = choice(edges)
    graph = removeEdge(graph, startNode, targetNode) 
    cycle = [startNode, targetNode]
    currentNode = targetNode
    while currentNode != startNode:
      edges = graph[currentNode]
      targetNode = choice(edges)
      graph = removeEdge(graph, currentNode, targetNode)
      currentNode = targetNode
      cycle.append(currentNode)
    while graph:
      possStarts = [(idx, node) for idx, node in enumerate(cycle) if node in graph]
      idx, newStart = choice(possStarts)
      newCycle = cycle[idx:] + cycle[1:idx+1]
      edges = graph[newStart]
      targetNode = choice(edges)
      graph = removeEdge(graph, newStart, targetNode)
      currentNode = targetNode
      newCycle.append(currentNode)
      while currentNode != newStart:
        edges = graph[currentNode]
        targetNode = choice(edges)
        graph = removeEdge(graph, currentNode, targetNode)
        currentNode = targetNode
        newCycle.append(currentNode)
      cycle = newCycle
    return(cycle)

def eulerianPath(graph): 
  degdiff = {}
  for node, edges in graph.items():
    if node in degdiff:
      degdiff[node] += len(edges)
    else:
      degdiff[node] = len(edges)
      
    for edge in edges:
      if edge in degdiff:
        degdiff[edge] -= 1
      else:
        degdiff[edge] = -1
        
  for node, diff in degdiff.items():
    if diff == -1:
      endingNode = node
      
  for node, diff in degdiff.items():
    if diff == 1:
      startingNode = node  
      
  if endingNode in graph:
    graph[endingNode].append(startingNode)
  else:
    graph[endingNode] = [startingNode]
    
  cycle = eulerianCycle(graph)
  i = 0
  while True:
    if cycle[i] == endingNode and cycle[i+1] == startingNode:
      break
    i += 1
  eulerPath = cycle[i+1:] + cycle[1:i+1]
  return eulerPath

def stringReconstruction(kmer,text):
    db = debruijn(text)
    path = eulerianPath(db)
    text = genome(path)
    return text

kmer,text = read_file(file)
output = stringReconstruction(kmer, text)
print(output)