#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    if len(arr) <= 2:
        return 0
    
    dp = [0  for _ in range(len(arr))]
    for i in range(len(arr)):
        if i < 2:
            dp[i] = max(arr[:i+1])
        else:
            dp[i] = max(dp[i-1], dp[i-2] + arr[i], arr[i])
    # print(dp)           
    return max(dp[-1], 0)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = maxSubsetSum(arr)
    print(res)

