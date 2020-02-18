#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 17:55:59 2020

@author: nenad
"""
from collections import defaultdict

class Node:
    def __init__(self, value):
        self._value = value
    
    def get_value(self):
        return self._value
    def set_value(self, value):
        self._value = value
    def __str__(self):
        return str(self._value)

class Graph:
    def __init__(self):
        self._vertices = defaultdict(lambda:[])
        self._is_weighted = False
    
    def add_edge(self, source, dest, weight = None):
        assert isinstance(source, Node) and isinstance(dest, Node)
        if weight is not None:
            # weighted graph
            if not self._is_weighted:
                self._is_weighted = True
            entry = (dest, weight)
        else:
            entry = dest
        
        self._vertices[source].append(entry)
        
    def _print_weighted_graph(self):
        for v, e in self._vertices.items():
            output = ','.join([str((entry[0].__str__(), entry[1])) for entry in e])
            print("Vertex {} -> {}".format(v, output))
    def _print_unweighted(self):
        for v, e in self._vertices.items():
            output = ','.join([str(entry.__str__()) for entry in e])
            print("Vertex {} -> {}".format(v, output))
    def print(self):
        if self._is_weighted:
            self._print_weighted_graph()
        else:
            self._print_unweighted()
        
            
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
g = Graph()
g.add_edge(n1, n3, 2)
g.add_edge(n2, n3, -2)
g.add_edge(n1, n4, 20)
g.add_edge(n3, n5, 100)
g.add_edge(n2, n6, 8)
g.add_edge(n4, n5, 3)
g.add_edge(n1, n5, 61)
g.add_edge(n7, n2, -75)
g.print()
    
    