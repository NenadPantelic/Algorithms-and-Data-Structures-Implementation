#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:32:34 2020

@author: nenad
"""


# Edit Distance problem

# find the minimum number of operations (insert, edit and delete) to convert one string s1, to another s2
def edit_distance(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    dp = [[0 for i in range(len1+1)] for j in range(len2+1)]
    
    dp[0] = list(range(len1+1))
    for i in range(len2+1):
        dp[i][0] = i
    # over s2
    for i in range(1, len2+1):
        # over s1
        for j in range(1, len1+1):
            #if i == 0 or j == 0:
            #    continue
            
            if s1[j-1] == s2[i-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
    print(get_changes(dp, s1, s2))         
    return dp[len2][len1]

def get_changes(dp, s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    changes = []
    i = len2
    j = len1
    #value = dp[i][j]
    while True:
        if i == 0 and j == 0:
            break
        value = dp[i][j]
        left = top = diag = None
        if i > 0 and j > 0:
            diag = dp[i-1][j-1]
        if i > 0:
            top = dp[i-1][j]
        if j > 0:
            left = dp[i][j-1]
        minn = min(left, top, diag)
        if minn == diag:    
            if value != diag:
                changes.insert(0, "{} -> {} at {}".format(s1[j-1], s2[i-1], j-1))
            i -= 1
            j -= 1
        elif minn == left:
            changes.insert(0, "delete {} at {}".format(s1[j-1], j-1))
            j -= 1
        else:
            changes.insert(0, "insert {} at {}".format(s2[i-1], j))
            i -= 1
    return changes
        
        

s1 = 'abcdef'
s2 = 'azced'
print(edit_distance(s1, s2))

s1 = 'abcdef'
s2 = 'azcedgw'
print(edit_distance(s1, s2))
