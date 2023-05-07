class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0 for _ in range(n)]
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
    

if __name__ == "__main__":
    test_cases = [[2, 2],
                  [3, 3]]
    
    solution = Solution()
    
    for test_case in test_cases:
        if solution.climbStairs(*test_case[:-1]) != test_case[-1]:
            print("FAIL")
            break
    print("SUCCESS")