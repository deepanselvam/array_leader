def printLeaders(arr, size):
    for i in range(size):
        j = i + 1
        while j < size:
            if arr[i] <= arr[j]:
                break
            j += 1
        if j == size:
            print(arr[i], end=" ")

n = int(input())
arr = list(map(int, input().split()))
printLeaders(arr, n)
