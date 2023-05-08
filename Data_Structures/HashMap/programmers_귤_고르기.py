# 프로그래머스 - 귤 고르기

from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    counter = Counter(tangerine)
    for num in sorted(counter.values(), reverse=True):
        k -= num
        answer += 1
        if k <= 0:
            return answer
    return answer


if __name__ == "__main__":
    test_cases = [[6, [1, 3, 2, 5, 4, 5, 2, 3], 3],
                  [4, [1, 3, 2, 5, 4, 5, 2, 3], 2],
                  [2, [1, 1, 1, 1, 2, 2, 2, 3],	1]]
    
    fail = False
    for test_case in test_cases:
        if solution(*test_case[:-1]) != test_case[-1]:
            print("FAIL")
            fail = True
            break

    if not fail:
        print("SUCCESS")
