n = int(input())
p = list(map(int, input().split()))

p.sort()

result = 0
past = 0

for i in p:
    result += past + i
    past += i

print(result)