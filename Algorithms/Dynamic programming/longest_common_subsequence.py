#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 13:47:44 2020

@author: nenad
"""

# longest common subsequence
def lcs(s1, s2):
    dp = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
    for i in range(len(s1)+1):
        for j in range(len(s2)+1):
            if i == 0 or j == 0:
                continue
            # elements are the same, take lcs(i-1, j-1) + 1 -> lcs(s1[:i][:j]) + 1
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                # take max value: lcs(i-1, j), lcs(i, j-1), so lcs(s1[:i], s2[:j-1]) and lcs(s1[:i-1][:j])
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
    #print(dp)                
    print(get_common_elements(dp, s1, s2))           
    return dp[len(s1)][len(s2)]

def get_common_elements(dp, s1, s2):
    i = len(s1); j = len(s2)
    value = dp[i][j]
    elements = []
    while True:
        if i == 0  and j == 0:
            break
        value = dp[i][j]
        left = top = None
        if i > 0:
            top = dp[i-1][j]
        if j > 0:
            left = dp[i][j-1]
        if value != left and value != top:
            elements.insert(0, s1[i-1])
            i -= 1
            j -= 1
        elif value == top:
            i -= 1
        elif value == left:
            j -= 1
    return elements
         
    

s1 = 'abcdaf'
s2 = 'acbcf'
print(lcs(s1, s2))