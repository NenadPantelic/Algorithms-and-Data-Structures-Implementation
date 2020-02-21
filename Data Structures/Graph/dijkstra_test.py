#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 14:21:05 2020

@author: nenad
"""
from dijkstra import dijkstra
from dijkstra_indexed_pq import dijkstra_optimized

def find_path(prev, dist, source, dest):
    path = []
    if dist[dest] == float('inf'):
        return path
    node = dest
    while node:
        path.append(node)
        node = prev[node]
    path.append(source)
    path.reverse()
    return path

from collections import defaultdict

graph = defaultdict(list)
graph[0].extend([(1,5), (2,1)])
graph[1].extend([(2,2), (3,3), (4,20)])
graph[2].extend([(1,3), (4,12)])
graph[3].extend([(2,3), (4,2), (5,6)])
graph[4].extend([(5,1)])
graph[5] = []
dist, prev = dijkstra(0, graph)
for i in range(6):
    print("Distance from source to node {}: {}".format(i,dist[i]))
    print("Path to this node = {}".format(find_path(prev, dist, 0,i)))

print("\nDijkstra with indexed pq\n")    
dist, prev = dijkstra_optimized(0, graph)
for i in range(6):
    print("Distance from source to node {}: {}".format(i,dist[i]))
    print("Path to this node = {}".format(find_path(prev, dist, 0,i)))