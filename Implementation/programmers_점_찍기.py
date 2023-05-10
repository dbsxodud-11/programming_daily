# 프로그래머스 - 점 찍기 (Lv.2)

import math

def solution(k, d):
    answer = 0
    
    for x in range(0, d+1, k):
        y_max = int(math.sqrt(d**2 - x**2)) // k
        answer += y_max + 1
    
    return answer


if __name__ == "__main__":
    test_cases = [[2, 4, 6],
                  [1, 5, 26]]
    
    fail = False
    for test_case in test_cases:
        if solution(*test_case[:-1]) != test_case[-1]:
            print("FAIL")
            fail = True
            break

    if not fail:
        print("SUCCESS")
