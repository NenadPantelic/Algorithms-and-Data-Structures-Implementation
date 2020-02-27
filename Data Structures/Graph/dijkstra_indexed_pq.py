#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 14:15:18 2020

@author: nenad
"""

# indexed priority queue

#O(1) search for the item with highest priority
#O(log n) removal of the item with highest priority
#O(log n) insertion of a new item

#O(1) lookup of any item by key
#O(log n) removal of any item
#O(log n) updating of any item’s priority level


from pqdict import minpq
# Complexity - O(Elog(V)) - E (num of edges); V (num of vertices)
def dijkstra_optimized(source, graph):
    # number of nodes in graph
    n = len(graph)
    visited = [False] * n
    prev = [None] * n
    # init distances
    dist = [float('inf')] * n
    # distance from source itself is 0
    dist[source] = 0
    # priority queue
    pq = minpq()
    # heapify regards first value
    pq[source] = 0
    while len(pq) != 0:
        # node with minimum distance
        curr_node, min_value = pq.popitem()
        visited[curr_node] = True
        for node, distance in graph[curr_node]:
            if visited[node]:
                continue
            new_dist = dist[curr_node] + distance
            # better distance - shorter
            if new_dist < dist[node]:
                dist[node] = new_dist
                # insert or update
                if pq.get(node, None):
                    pq[node] = new_dist
                else:
                    pq[node] = new_dist
                prev[node] = curr_node                
    return dist, prev