class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in range(len(s)//2):
            if s[i] != s[len(s)-i-1]:
                return False
        return True
    
    def longestPalindrome(self, s: str) -> str:
        # # naive approach: O(n^3)
        # max_length = 0
        # answer = ""
        # for i in range(len(s)):
        #     for j in range(i+1, len(s)+1):
        #         substring = s[i:j]
        #         if self.isPalindrome(substring):
        #             if max_length < len(substring):
        #                 max_length = len(substring)
        #                 answer = substring
        # return answer   

        # dynamic programming: O(n^2)
        answer = s[0]

        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if i == j:
                    dp[i][j] = True
                else:
                    if s[i] == s[j]:
                        if i+1 == j or dp[i+1][j-1]:
                            dp[i][j] = True
                            if len(answer) < len(s[i:j+1]):
                                answer = s[i:j+1]
        return answer

if __name__ == "__main__":
    test_cases = [["babad", "aba"],
                  ["cbbd", "bb"]]
    
    solution = Solution()
    
    fail = False
    for test_case in test_cases:
        if solution.longestPalindrome(*test_case[:-1]) != test_case[-1]:
            print("FAIL")
            fail = True
            break
        
    if not fail:
        print("SUCCESS")
