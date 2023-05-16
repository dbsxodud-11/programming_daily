# 프로그래머스 - 쌍둥이 빌딩 숲 (Lv.4)

def solution(n, count):
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for c in range(i, -1, -1):
            if i == 0 and c == 0:
                dp[0][0] = 1
            else:
                dp[i][c] = dp[i-1][c-1] + dp[i-1][c] * i * 2
    # print(dp)
    return dp[n-1][count-1] % 1000000007


if __name__ == "__main__":
    test_cases = [[3, 1, 8],
                  [3, 2, 6],
                  [3, 3, 1]]
    
    fail = False
    for test_case in test_cases:
        if solution(*test_case[:-1]) != test_case[-1]:
            print("FAIL")
            fail = True
            break

    if not fail:
        print("SUCCESS")