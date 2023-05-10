# LeetCode - Median of Two Sorted Arrays (Hard)

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        l = 0
        r = len(A) - 1
        t = len(A) + len(B)
        m = t // 2
        while True:
            i = (l + r) // 2
            j = m - i - 2
            A_left = A[i] if i >= 0 else float("-inf")
            A_right = A[i+1] if (i+1) < len(A) else float("inf")
            B_left = B[j] if j >= 0 else float("-inf")
            B_right = B[j+1] if (j+1) < len(B) else float("inf")

            if A_left > B_right:
                r = i - 1
            if B_left > A_right:
                l = i + 1
            
            if A_left <= B_right and B_left <= A_right:
                if t % 2 == 0:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
                else:
                    return min(A_right, B_right)


if __name__ == "__main__":
    test_cases = [[[1, 3], [2], 2],
                  [[1, 2], [3, 4], 2.5]]
    
    solution = Solution()
    
    for test_case in test_cases:
        if solution.findMedianSortedArrays(*test_case[:-1]) != test_case[-1]:
            print("FAIL")
            break
    print("SUCCESS")
