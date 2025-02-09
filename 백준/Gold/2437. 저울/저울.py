import sys

input=sys.stdin.readline

input()
weights=list(map(int, input().split(" ")))
weights.sort()

possible=0

for i in weights:
    if i>possible+1:
        break
    possible+=i

print(possible+1)