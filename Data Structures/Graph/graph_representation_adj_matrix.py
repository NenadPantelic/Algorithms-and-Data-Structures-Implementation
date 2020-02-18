#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 18:24:02 2020

@author: nenad
"""


class Node:
    def __init__(self, value):
        self._value = value
    
    def get_value(self):
        return self._value
    def set_value(self, value):
        self._value = value
    def __str__(self):
        return str(self._value)
    
    
class UnweightedGraph:
    def __init__(self, size):
        self._vertices = [[0] * size for i in range(size)]
    
    def add_edge(self, source, dest):
        assert isinstance(source, Node) and isinstance(dest, Node)  
        self._vertices[source.get_value()-1][dest.get_value()-1] = 1
        
    def print(self):
        for i in range(len(self._vertices)):
            print("Vertex: {} -> {}".format(i+1, self._vertices[i]))
            
            
class WeightedGraph(UnweightedGraph):
    def __init__(self, size):
        self._vertices = [[None] * size for i in range(size)]
        
    def add_edge(self, source, dest, weight):
        assert isinstance(source, Node) and isinstance(dest, Node)  
        self._vertices[source.get_value()-1][dest.get_value()-1] = weight
    
# unweighted
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
g = UnweightedGraph(7)
#print(g._vertices)
g.add_edge(n1, n3)
g.add_edge(n2, n3)
g.add_edge(n1, n4)
g.add_edge(n3, n5)
g.add_edge(n2, n6)
g.add_edge(n4, n5)
g.add_edge(n1, n5)
g.add_edge(n7, n2)
g.add_edge(n5, n7)
g.print()


# weighted
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
g = WeightedGraph(7)
g.add_edge(n1, n3, 2)
g.add_edge(n2, n3, -2)
g.add_edge(n1, n4, 20)
g.add_edge(n3, n5, 100)
g.add_edge(n2, n6, 8)
g.add_edge(n4, n5, 3)
g.add_edge(n1, n5, 61)
g.add_edge(n7, n2, -75)
g.print()