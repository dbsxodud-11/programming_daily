# 백준 - 다리 놓기

from itertools import combinations

def solution(n, m):
    # # dp[i]: n개의 다리를 i개의 지역에 놓을 수 있는 경우의 수

    dp = [0 for _ in range(m)]
    for i in range(1, m+1):
        if i < n:
            dp[i-1] = 0
        elif i == n:
            dp[i-1] = 1
        else:
            dp[i-1] = dp[i-2] * i // (i-n) 
    # print(dp)
    return dp[-1]


if __name__ == "__main__":
    num_test_cases = int(input())
    test_cases = []
    for i in range(num_test_cases):
        test_cases.append(map(int, input().strip('\n').split()))

    for test_case in test_cases:
        print(solution(*test_case))