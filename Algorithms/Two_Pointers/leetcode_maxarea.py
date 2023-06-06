from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(height) - 1
        while l < r:
            current = (r-l) * min(height[l], height[r])
            max_area = max(max_area, current)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return max_area
    

if __name__ == "__main__":
    test_cases = [[[1,8,6,2,5,4,8,3,7], 49],
                  [[1, 1], 1]]
    
    solution = Solution()
    
    fail = False
    for test_case in test_cases:
        if solution.maxArea(*test_case[:-1]) != test_case[-1]:
            print("FAIL")
            fail = True
            break
        
    if not fail:
        print("SUCCESS")
