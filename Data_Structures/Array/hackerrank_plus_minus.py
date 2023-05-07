# Hackerrank - Plus Minus

def plusMinus(arr):
    # Write your code here
    plus, zero, minus = 0, 0, 0
    for elem in arr:
        if elem > 0:
            plus += 1
        elif elem == 0:
            zero += 1
        else:
            minus += 1
    
    print(f"{plus / len(arr):.6f}")
    print(f"{minus / len(arr):.6f}")
    print(f"{zero / len(arr):.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)