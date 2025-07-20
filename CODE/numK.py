n = int(input())
k = int(input())

# horizon = []
# flat = []

# for i in range(1, n+1):
#     for j in range(1, n+1):
#         horizon.append(i * j)
#     flat.append(horizon)
#     horizon = []

# print(flat)

res = 0
l, r = 1, n*n

while l <= r:
    mid = (l+r) // 2
    cnt = 0
    for i in range(1, n+1):
        cnt += min(n, (mid-1) // i)
    if cnt <= k:
        res = max(res, mid)
        l = mid + 1
    else:
        r = mid - 1

print(res)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       