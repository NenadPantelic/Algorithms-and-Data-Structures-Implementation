#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 12:13:43 2020

@author: nenad
"""


from heapq import heappush, heappop
# optimize it with indexed pq
def dijkstra(source, graph):
    # number of nodes in graph
    n = len(graph)
    visited = [False] * n
    prev = [None] * n
    # init distances
    dist = [float('inf')] * n
    # distance from source itself is 0
    dist[source] = 0
    # priority queue
    pq = []
    # heapify with with dist values as comparation value
    heappush(pq, (0, source))
    while len(pq) != 0:
        # node with minimum distance
        min_value, curr_node = heappop(pq)
        visited[curr_node] = True
        for node, distance in graph[curr_node]:
            if visited[node]:
                continue
            new_dist = dist[curr_node] + distance
            if new_dist < dist[node]:
                dist[node] = new_dist
                prev[node] = curr_node
                heappush(pq, (new_dist, node))
                
    return dist, prev


    

    