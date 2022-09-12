#!/usr/bin/env python3
"""
Created on Sat Sep 9 20:23:17 2022

@author: radleyrp
"""
"""
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
"""
def contigsP(paths):
    contigs = []
    for path in paths:
        nodes = path.strip('\n')
        nodes = nodes.split(' ')
        text = ""
        for i in range(len(nodes)):
            text = text[0:i] + nodes[i]
        contigs.append(text)
    contigs.sort()
    return contigs

def debruijn(kmers):
    result = {}
    kmers.sort()
    
    for i in range(len(kmers)):
        prefix = kmers[i][0:-1]
        suffix = kmers[i][1:]
        if(prefix[1:] == suffix[:-1]):
            if prefix in result.keys():
                result[prefix] += ("," + suffix)
            else:
                result[prefix] = prefix + " " + suffix
    return result.values()

def maximalNonBranchingPaths(adjacency_list):
    graph = {}
    for line in adjacency_list:
        node = line.strip('\n')
        node = node.split(' ')
        graph.setdefault(node[0],[])
        for num in node[1].split(','):
            graph[node[0]].append(num)
    
    degree = inOut(graph)
    paths = []
    for vertex,edge in graph.items():
        if not oneInOneOut(vertex, degree):
            if degree[1].get(vertex,0) > 0:
                for nextV in graph[vertex]:
                    nonBranchingPath = str(vertex) + " " + str(nextV)
                    while oneInOneOut(nextV, degree):
                        for extendEdge in graph[nextV]:
                            nonBranchingPath += " " + extendEdge
                            nextV = extendEdge
                    paths.append(nonBranchingPath)
        else:
            if not visited(vertex, paths): 
                temp_cycle = cycle(vertex, degree, graph)
                if temp_cycle:
                    paths.append(temp_cycle)
    return paths

def oneInOneOut(vertex, degree):
    deg_in = degree[0].get(vertex,0)
    deg_out = degree[1].get(vertex,0)
    return (deg_in == 1) and (deg_out == 1)

def visited(vertex, paths):
    for path in paths:
        if vertex in path:
            return True
    return False

def cycle(vertex, degree, graph):
    cycle = [vertex]
    while oneInOneOut(cycle[-1], degree):
        cycle.append(graph[cycle[-1]][0])
        if cycle[0]==cycle[-1]:
            cycle_path = ""
            for each in cycle:
                cycle_path += each + " "
            return cycle_path[:-1]
    return None
    
def inOut(graph):
    inDegree = {}
    outDegree = {}
    for key, value in graph.items():
        outDegree[key] = len(value)
        for i in value:
            inDegree[i] = inDegree.get(i,0)+1
    return (inDegree,outDegree)

def read_file(file_name):
    content_list=[]
    with open(file_name, "r") as file:
        while True:
            line = file.readline()
            line=line.strip()
            content_list.append(line.split(","))
            if not line:
                break
    return content_list 

def result(kmers):
    graph = debruijn(kmers)
    paths = maximalNonBranchingPaths(graph)
    contigs = contigsP(paths)
    return contigs


#kmers = [line.split() for line in open("../datasets/dataset_746270_5.txt")]

#print(kmers)


file = "../datasets/dataset_746270_5.txt"

kmers = read_file(file)
kmers=kmers[0][0].split(" ")
#print(kmers)



#kmers = ['GAGA', 'AGAG', 'AACG', 'ACGT', 'ACGG']

print('\n'.join(result(kmers)))
#print(contig_generation_problem(kmers))