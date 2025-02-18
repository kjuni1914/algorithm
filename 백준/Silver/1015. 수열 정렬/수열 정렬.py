import sys
input=sys.stdin.readline

N=int(input())

nums=list(map(int, input().split()))

snums=sorted(nums)
idx={i+1:[] for i in range(1001)}
for i in range(N-1, -1, -1):
    idx[snums[i]].append(i)

res=""
for i in nums:
    res+=str(idx[i].pop())+" "

print(res)