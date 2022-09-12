#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 15:40:23 2022

@author: radleyrp
"""

file ='../datasets/dataset_746268_6.txt'

from random import choice


with open('../datasets/dataset_746268_6.txt') as f:
    input = f.readlines()
    
edges = [tuple(edge.split(': ')) for edge in input if edge]
edges = [(int(node[0]), [int(i) for i in node[1].split(' ')]) for node in edges]
edgesnv = {i: j for i, j in edges}

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
      i, newStart = choice(possStarts)
      newCycle = cycle[i:] + cycle[1:i+1]
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

cycle = eulerianPath(edgesnv)
print(*cycle)
#print("->".join(eulerianPath(graph)))