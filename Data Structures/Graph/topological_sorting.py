#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 11:35:00 2020

@author: nenad
"""

from collections import defaultdict

def topological_sorting(graph):
    n = len(graph)
    visited = {node:False for node in graph}
    ordering = [0] * n
    # ordering index
    i = n-1
    for node in graph:
        if visited[node]:
            continue
        visited_nodes = []
        dfs(node, visited, visited_nodes, graph)
        for vis_node in visited_nodes:
            ordering[i] = vis_node
            i -= 1
    return ordering
    
def dfs(node, visited, visited_nodes, graph):    
    visited[node] = True
    neighbours = graph[node]
    for neighbour in neighbours:
        if not visited[neighbour]:
            dfs(neighbour, visited, visited_nodes, graph)
    visited_nodes.append(node)
    
    
graph = defaultdict(list)
graph['C'].extend(['A','B'])
graph['A'].append('D')
graph['B'].append('D')
graph['E'].extend(['A','D', 'F'])
graph['D'].extend(['H','G'])
graph['G'].append('I')
graph['H'].extend(['I','J'])
graph['F'].extend(['J','K'])
graph['J'].extend(['M','L'])
graph['K'].append('J')
graph['I'].append('L')
graph['L'] = []
graph['M'] = []

print(topological_sorting(graph))