#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 10:02:24 2022

@author: radleyrp
"""
from random import choice
#file ='../datasets/euGraph.txt'


with open('../datasets/euGraph.txt') as f:
    input = f.readlines()


def removeEdge(graph, startNode, targetNode):
  graph[startNode].remove(targetNode)
  if not graph[startNode]:
    del graph[startNode]
  return graph

edges = [tuple(edge.split(': ')) for edge in input if edge]
edges = [(int(node[0]), [int(i) for i in node[1].split(' ')]) for node in edges]
edgesnv = {i: j for i, j in edges}


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

    
cycle = eulerianCycle(edgesnv)
print(*cycle)

    