class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        levels = [[] for _ in range(numRows)]
        for i in range(0, len(s), 2*numRows-2):
            for j in range(min(numRows, len(s)-i)):
                levels[j].append(s[i+j])
            for j in range(min(numRows-2, len(s)-i-numRows)):
                levels[numRows-j-2].append(s[i+j+numRows])
        return "".join(["".join(level) for level in levels])
    
    
if __name__ == "__main__":
    test_cases = [["PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"],
                  ["PAYPALISHIRING", 4, "PINALSIGYAHRPI"],
                  ["A", 1, "A"]]
    
    solution = Solution()
    
    fail = False
    for test_case in test_cases:
        if solution.convert(*test_case[:-1]) != test_case[-1]:
            print("FAIL")
            fail = True
            break
    
    if not fail:
        print("SUCCESS")
