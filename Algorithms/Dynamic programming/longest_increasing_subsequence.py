#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 20:14:33 2020

@author: nenad
"""

# for the given sequence, determine longest increasing subsequence
def longest_increasing_subsequence(arr):
    n = len(arr)
    dp = [1] * n
    solution = list(range(n))
    for i in range(n):
        for j in range(0, i):
            if arr[j] < arr[i]:
                # update value if it is better than current one (dp[last element in increasing sequence so far] + 1)
                maxx = max(dp[i], dp[j] + 1)
                if maxx == dp[j] + 1:
                    # write what is the previous element in that increasing subsequence;
                    solution[i] = j
                dp[i] = maxx 
    return dp, solution


        
def get_longest_incr_sub(solution, max_index):
    index = max_index
    subsequence = [index]
    # greatest value is the length of the LIS
    while index != solution[index]:
        index = solution[index]
        subsequence.insert(0, index)
    return subsequence
        
    
def get_longest_incr_len(dp):
    maxx = 1
    maxx_index = 0  
    for i in range(len(dp)):
        if dp[i] > maxx:
            maxx = dp[i]
            maxx_index = i
    return maxx_index

# Test 1
seq = [3,4,-1,0,6,2,3]
dp, solution = longest_increasing_subsequence(seq)
#print(dp)
index = get_longest_incr_len(dp)
print("Longest increasing subsequence length: {}".format(dp[index]))
indices = get_longest_incr_sub(solution, index)
print("Longest increasing subsequence:", end=" ")
for ind in indices:
    print(seq[ind], end = " ")
    
print()
# Test 1
seq = [2,5,1,8,3]
dp, solution = longest_increasing_subsequence(seq)
#print(dp)
index = get_longest_incr_len(dp)
print("Longest increasing subsequence length: {}".format(dp[index]))
indices = get_longest_incr_sub(solution, index)
print("Longest increasing subsequence:", end=" ")
for ind in indices:
    print(seq[ind], end = " ")
    
print()