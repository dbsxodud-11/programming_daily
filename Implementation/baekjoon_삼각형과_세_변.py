# baekjoon - 삼각형과 세 변

def solution(triangles):
    for triangle in triangles:
        triangle.sort()
        a, b, c = triangle
        # 1. Invalid
        if c >= a+b:
            print("Invalid")
        # 2. Equilateral
        elif a == c:
            print("Equilateral")
        # 3. Isosceles
        elif a == b or b == c:
            print("Isosceles")
        # 4. Scalene
        else:
            print("Scalene")


if __name__ == "__main__":
    triangles = []
    while True:
        a, b, c = map(int, input().strip("\n").split(" "))
        if a == 0 and b == 0 and c == 0:
            break
        triangles.append([a, b, c])
    
    solution(triangles)