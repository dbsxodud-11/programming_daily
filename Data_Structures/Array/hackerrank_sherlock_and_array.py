# Hackerrank - Sherlock and Array (Basic)

import math
import os
import random
import re
import sys
from itertools import accumulate

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    # Write your code here
    left_acc = [0] + list(accumulate(arr))
    right_acc = list(accumulate(arr[::-1]))[::-1] + [0]
    
    for i, elem in enumerate(arr):
        if left_acc[i] == right_acc[i+1]:
            return "YES"
    return "NO"

if __name__ == '__main__':
    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        print(result + '\n')
