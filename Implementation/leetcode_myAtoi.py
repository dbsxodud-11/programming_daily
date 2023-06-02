class Solution:
    def myAtoi(self, s: str) -> int:
        # step 1. ignore leading whitespace
        s = s.lstrip()
        
        if len(s) == 0:
            return 0

        # step 2. check sign
        negative = False
        if s[0] == "-":
            negative = True
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]

        # step 3. check digit
        answer = 0
        for i in range(len(s)):
            if not str.isdigit(s[i]):
                break
            else:
                answer = answer * 10 + int(s[i])
        
        # step 4. clamp
        answer = max(-answer, -2**31) if negative else min(answer, 2**31-1)
        return answer
    
if __name__ == "__main__":
    test_cases = [["42", 42],
                  ["   -42", -42],
                  ["4193 with words", 4193],
                  ["  0 123", 0]]
    
    solution = Solution()
    
    fail = False
    for test_case in test_cases:
        if solution.myAtoi(*test_case[:-1]) != test_case[-1]:
            print("FAIL")
            fail = True
            break
    
    if not fail:
        print("SUCCESS")
