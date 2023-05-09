# 프로그래머스 - 미로 탈출 (Lv.2)

from collections import deque

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find_start(maps):
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == "S":
                return [i, j, 0]

def solution(maps):
    answer = 0
    
    start = find_start(maps)
    lever = None
    
    l_dfs = deque()
    counts = [[float("inf") for _ in range(len(maps[0]))] for _ in range(len(maps))]
    l_dfs.append(start)
    counts[start[0]][start[1]] = start[2]
    while len(l_dfs) > 0:
        i, j, path_len = l_dfs.popleft()
        if maps[i][j] == "L":
            lever = [i, j, path_len]
            break
        for dx, dy in DIRS:
            if i+dx >= 0 and i+dx < len(maps) and j+dy >= 0 and j+dy < len(maps[i]) and maps[i+dx][j+dy] != "X" and path_len+1 < counts[i+dx][j+dy]:
                counts[i+dx][j+dy] = path_len+1
                l_dfs.append([i+dx, j+dy, path_len+1])
    
    if lever is None:
        return -1

    e_dfs = deque()
    counts = [[float("inf") for _ in range(len(maps[0]))] for _ in range(len(maps))]
    e_dfs.append(lever)
    counts[lever[0]][lever[1]] = lever[2]
    while len(e_dfs) > 0:
        i, j, path_len = e_dfs.popleft()
        if maps[i][j] == "E":
            return path_len
        for dx, dy in DIRS:
            if i+dx >= 0 and i+dx < len(maps) and j+dy >= 0 and j+dy < len(maps[i]) and maps[i+dx][j+dy] != "X" and path_len+1 < counts[i+dx][j+dy]:
                counts[i+dx][j+dy] = path_len+1
                e_dfs.append([i+dx, j+dy, path_len+1])
    return -1


if __name__ == "__main__":
    test_cases = [[["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"], 16],
                  [["LOOXS","OOOOX","OOOOO","OOOOO","EOOOO"], -1]]
    
    fail = False
    for test_case in test_cases:
        if solution(*test_case[:-1]) != test_case[-1]:
            print("FAIL")
            fail = True
            break

    if not fail:
        print("SUCCESS")
