# LeetCode - Longest Substring Without Repeating Characters (Medium)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start_idx = 0
        curr_length = 0
        max_length = 0
        char2idx = {}

        for i, c in enumerate(s):
            if c in char2idx and char2idx[c] >= start_idx:
                start_idx = char2idx[c] + 1
            curr_length = i - start_idx + 1
            max_length = max(curr_length, max_length)
            char2idx[c] = i

        return max_length

if __name__ == "__main__":
    test_cases = [["abcabcbb", 3],
                  ["bbbbb", 1],
                  ["pwwkew", 3]]
    
    solution = Solution()
    
    fail = False
    for test_case in test_cases:
        if solution.lengthOfLongestSubstring(*test_case[:-1]) != test_case[-1]:
            print("FAIL")
            fail = True
            break
    
    if not fail:
        print("SUCCESS")
