# 프로그래머스 - 롤케이크 자르기 (Lv.2)

from collections import defaultdict

def solution(topping):
    answer = 0
    
    # naive method
    player1_set = set()
    player2_set = set(topping)
    top2count = defaultdict(int)
    for top in topping:
        top2count[top] += 1
    fair = False
    
    for top in topping:
        player1_set.add(top)
        top2count[top] -= 1
        if top2count[top] == 0:
            top2count.pop(top)
            player2_set.remove(top)

        if len(player1_set) == len(player2_set):
            fair = True
            answer += 1
        else:
            if fair:
                break
    
    return answer


if __name__ == "__main__":
    test_cases = [[[1, 2, 1, 3, 1, 4, 1, 2], 2],
                  [[1, 2, 3, 1, 4],	0]]
    
    fail = False
    for test_case in test_cases:
        if solution(*test_case[:-1]) != test_case[-1]:
            print("FAIL")
            fail = True
            break

    if not fail:
        print("SUCCESS")