class Solution:
    def intToRoman(self, num: int) -> str:
        
        numbers = []
        while num != 0:
            i = num % 10
            num = num // 10
            numbers.append(i)

        romans = ["I", "V", "X", "L", "C", "D", "M"]

        answer = ""
        for i, number in enumerate(numbers):
            if number < 4:
                # answer += "I" * number
                answer += romans[i*2] * number
            elif number == 4:
                # answer += "IV"
                answer += romans[i*2+1] + romans[i*2]
            elif number == 5:
                # answer += "V"
                answer += romans[i*2+1]
            elif number < 9:
                # answer += "V" + "I" * (number - 5)
                answer += romans[i*2] * (number - 5) + romans[i*2+1]
            else:
                # answer += "IX"
                answer += romans[i*2+2] + romans[i*2]
        return answer[::-1]
    
    
if __name__ == "__main__":
    test_cases = [[3, "III"],
                  [58, "LVIII"],
                  [1994, "MCMXCIV"]]
    
    solution = Solution()
    
    fail = False
    for test_case in test_cases:
        if solution.intToRoman(*test_case[:-1]) != test_case[-1]:
            print("FAIL")
            fail = True
            break
    
    if not fail:
        print("SUCCESS")
