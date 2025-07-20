import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

m = int(input())
qarr = list(map(int, input().split()))

for i in qarr:
    if bisect_right(arr, i) - bisect_left(arr, i) > 0:
        print(1)
    else:
        print(0)
