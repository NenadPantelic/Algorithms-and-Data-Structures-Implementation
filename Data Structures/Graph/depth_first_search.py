#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 18:59:56 2020

@author: nenad
"""

from collections import defaultdict
graph = defaultdict(lambda:[])
#undirected graph
n = 13
graph[0].append(1)
graph[1].append(0)
graph[0].append(9)
graph[9].append(0)

graph[1].append(8)
graph[8].append(1)
graph[9].append(8)
graph[8].append(9)
graph[8].append(7)
graph[7].append(8)
graph[7].append(10)
graph[7].append(11)
graph[10].append(7)
graph[11].append(7)
graph[11].append(10)
graph[10].append(11)
graph[7].append(3)
graph[7].append(6)
graph[3].append(7)
graph[6].append(7)
graph[3].append(5)
graph[6].append(5)
graph[5].append(3)
graph[5].append(6)
graph[3].append(2)
graph[3].append(4)
graph[2].append(3)
graph[4].append(3)
print(graph)

visited = [False] * n
def dfs(start_node):
    if visited[start_node]:
        return
    visited[start_node] = True
    print(start_node)
    neighbours = graph[start_node]
    for node in neighbours:
        dfs(node)

start_node = 0
dfs(start_node)

    