# 프로그래머스 - N으로 표현

def calculate(set1, set2):
    set3 = set()
    for elem1 in set1:
        for elem2 in set2:
            set3.add(elem1 + elem2)
            set3.add(elem1 - elem2)
            set3.add(elem2 - elem1)
            set3.add(elem1 * elem2)
            if elem2 > 0:
                set3.add(elem1 / elem2)
            if elem1 > 0:
                set3.add(elem2 / elem1)
    return set3

def solution(N, number):
    # N을 최대 8번까지 활용할 수 있음. N을 k번 활용해 얻을 수 있는 모든 숫자를 저장해 두고, 
    # k+1번 활용해 얻을 수 있는 숫자를 1 ~ k번 활용해 얻을 수 있는 숫자들을 활용해 계산 - Dynamic Programming
    possible_numbers = [set() for _ in range(8)]
    
    for i in range(8):
        if i == 0:
            possible_numbers[i].add(N)
        else:
            possible_numbers[i].add(int(str(N) * (i+1)))
            for j in range(i):
                possible_numbers[i].update(calculate(possible_numbers[j],
                                                     possible_numbers[i-1-j]))
        if number in possible_numbers[i]:
            return i+1
    return -1


if __name__ == "__main__":
    test_cases = [[5, 12, 4],
                  [2, 11, 3]]
    
    fail = False
    for test_case in test_cases:
        if solution(*test_case[:-1]) != test_case[-1]:
            print("FAIL")
            fail = True
            break

    if not fail:
        print("SUCCESS")