# baekjoon - ZOAC 4
import math

def solution(w, h, n, m):
    return math.ceil(w / (n+1)) * math.ceil(h / (m+1))

if __name__ == "__main__":
    w, h, n, m = map(int, input().strip('\n').split(" "))
    print(solution(w, h, n, m))
