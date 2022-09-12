#!/usr/bin/env python3
"""
Created on Thu Sep  8 17:42:42 2022

@author: radleyrp
"""

from random import choice

"""
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
"""

def binary(k):
    return [bin(i)[2:].zfill(k) for i in range(2**k)]

def relation(k):
    nodes = binary(k-1)
    data = {}
    for item in nodes:
        add1 = item[1:]+'0'
        add2 = item[1:]+'1'
        data[item] = [add1,add2]
    return data

def cycle(data):
    node = choice(list(data.keys()))
    nextNode = choice(list(data[node]))
    cycle = [node]
    while len(data) != 0:
        try:
            cycle.append(nextNode)
            if len(data[node]) > 1:
                data[node].remove(nextNode)
            else:
                del data[node]
            node = nextNode
            nextNode = choice(data[node])
            if nextNode == cycle[0] and nextNode == cycle[-1]:
                break
        except:
            break
    return (cycle,data)

def unJoinCycle(data,node):
    choose = data[node]
    nextNode = choice(choose)
    cycle = [node]
    while len(data) != 0:
        try:
            cycle.append(nextNode)
            if len(data[node]) > 1:
                data[node].remove(nextNode)
            else:
                del data[node]
            node = nextNode
            nextNode = choice(data[node])
            if nextNode == cycle[0] and nextNode == cycle[-1]:
                break
        except:
            break
    return (cycle,data)

def joinCycle(Cycle,newCycle):
    index = Cycle.index(newCycle[0])
    return Cycle[:index]+newCycle+Cycle[index+1:]

def eulerianCycle(data,k):
    Cycle,unCycle = cycle(data)
    while len(unCycle) != 0:
        keys = unCycle.keys()
        potential = list(set(Cycle)&set(keys))
        newStart = choice(potential)
        newCycle,unCycle = unJoinCycle(unCycle,newStart)
        Cycle = joinCycle(Cycle,newCycle)
    return Cycle

def result(path):
    text = ''.join([item[-1] for item in path[1:]])
    return text



k = 9
data = relation(k)
#path = eulerianCycle(data)
path = eulerianCycle(data,k)
results = result(path)
print(results)