#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 14:26:25 2020

@author: nenad
"""
# Complexity - O(V^3) -> V = number of vertices

def bellman_ford(graph, source):
    n = len(graph)
    # init dist values to infinity
    dist = [float("inf")] * n
    # source distance from itself is 0
    dist[source] = 0
    for i in range(n-1):
        for node in graph:
            neighs = graph[node]
            for neigh, distance in neighs:
                # relax edge (update dist with shorter path)
                if dist[node] + distance < dist[neigh]:
                    dist[neigh] = dist[node] + distance
    # repeat BF again to find nodes caught in a neg cycle
    for i in range(n-1):
        for node in graph:
            neighs = graph[node]
            for neigh, distance in neighs:
                # relax edge (update dist with shorter path)
                if dist[node] + distance < dist[neigh]:
                    dist[neigh] = float("-inf")
    return dist
                    
                    
from collections import defaultdict
graph = defaultdict(list)
graph[0].append((1,5))
graph[1].extend([(2,20), (5,30), (6,60)])
graph[2].extend([(3,10), (4,75)])
graph[3].append((2,-15))
graph[4].append((9,100))
graph[5].extend([(4,25),(6,5),(8,50)])
graph[6].append((7,-50))
graph[7].append((8, -10))
graph[8] = []
graph[9] = []
print(bellman_ford(graph, 0))

    
            