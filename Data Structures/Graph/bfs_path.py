#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 21:14:23 2020

@author: nenad
"""
from collections import deque, defaultdict


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



def bfs_path(s,e, graph):
    '''
    

    Parameters
    ----------
    s : int (node)
        source node
    e : int (node)
        destination node

    Returns
    -------
    Path between s and e, if exists

    '''
    # do the bfs
    prev_list = bfs(s, graph)
    # path reconstruction (from s to e)
    path = reconstruct_path(s, e, prev_list)
    return path
    

def bfs(s, graph):
    visited = [False] * len(graph)
    prev = [None] * len(graph)
    visited[s] = True
    q = deque()
    q.append(s)
    
    while len(q) != 0:
        node = q.popleft()
        neighbours = graph[node]
        visited[node] = True
        # check every unvisited neighbour
        for neighbour in neighbours:
            if not visited[neighbour]:
                # set previous node
                prev[neighbour] = node
                # visit node
                visited[neighbour] = True
                q.append(neighbour)
                
    return prev

def reconstruct_path(s,e,prev):
    path = []
    at = e
    # check all nodes in prev until you reach s (start node); this was first node we examined in bfs
    while at != None:
        path.append(at)
        at = prev[at]
    # reverse path (we started from e (dest node))
    path.reverse()
    # check if there is a path
    if path[0] != s:
        return []
    return path


print(bfs_path(8,4, graph))
print(bfs_path(11,0, graph))


    
    
    

    