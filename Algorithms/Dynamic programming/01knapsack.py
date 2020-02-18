#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 12:59:42 2020

@author: nenad
"""


# 0-1 knapsack problem

def knapsack(weights, values, Weight):
    # weights and values arrays have the same length
    n = len(weights)
    dp = [[0 for i in range(Weight+1)] for j in range(n+1)]
    
    for i in range(n+1):
        for j in range(Weight+1):
            if i == 0 or j == 0:
                continue
            # ith item weight cannot contribute to weight j
            if j < weights[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i-1]] + values[i-1])
    print_items(dp, weights, values)
    return dp[n][Weight]

def print_items(table,weights, values):
    res = table[-1][-1]
    n = len(weights)
    weight = len(table[0])-1
    for i in range(n, 0, -1):
        if res <= 0:
            break
        # same as previous row
        if res == table[i-1][weight]:
            continue
        else:
            print(i-1)
        res -= values[i-1]
        weight -= weights[i-1]
        
            
val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
print(knapsack(wt, val, W))
                                            
                