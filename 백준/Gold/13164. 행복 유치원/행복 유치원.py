import sys

input=sys.stdin.readline

N, K=map(int, input().split())

childs=list(map(int, input().split()))
difference=[childs[i+1]-childs[i] for i in range(N-1)]
difference.sort(reverse=True)

print(sum(difference[K-1:]))