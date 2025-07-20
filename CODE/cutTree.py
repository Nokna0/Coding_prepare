import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))

result = 0
l, r = 0, max(arr)


while l <= r:
    mid = (l + r) // 2
    sum = 0
    for i in arr:
        sum += max(i - mid, 0)

    if sum >= m:
        result = max(result, mid)
        l = mid + 1
    else:
        r = mid - 1

print(result)
