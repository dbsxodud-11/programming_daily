# 프로그래머스 - 디펜스 게임

from heapq import heappush, heappop

def solution(n, k, enemy):
    if k >= len(enemy):
        return len(enemy)
    
    heap = []
    answer = 0
    for i in range(k):
        heappush(heap, enemy[i])
        answer += 1
    
    while n > 0 and answer < len(enemy):
        heappush(heap, enemy[answer])
        min_round = heappop(heap)
        if n >= min_round:
            answer += 1
        n -= min_round
    
    return answer


if __name__ == "__main__":
    test_cases = [[7, 3, [4, 2, 4, 5, 3, 3, 1], 5],
                  [2, 4, [3, 3, 3, 3], 4]]
    
    fail = False
    for test_case in test_cases:
        if solution(*test_case[:-1]) != test_case[-1]:
            print("FAIL")
            fail = True
            break

    if not fail:
        print("SUCCESS")