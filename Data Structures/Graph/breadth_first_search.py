#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 20:52:11 2020

@author: nenad
"""


from collections import defaultdict
graph = defaultdict(list)
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
#print(graph)

from collections import deque
def bfs(start_node, graph):
    q = deque()
    q.append(start_node)
    visited = [False] * len(graph)
    visited[start_node] = True
    while len(q) != 0:
        # take last element 
        node = q.popleft()
        print(node, end=" ")
        # examine all of it's neighbours
        neighbours = graph[node]
        for neighbour in neighbours:
            if not visited[neighbour]:
                visited[neighbour] = True
                # enqueue neighbour
                q.append(neighbour)
                
                
bfs(0, graph)
print()    
#g = Graph() 
g = defaultdict(list)
g[0].append(1)
g[0].append(2)
g[1].append(2)
g[2].append(0)
g[2].append(3)
g[3].append(3)
bfs(2, g)
