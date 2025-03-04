import sys

input=sys.stdin.readline
N=int(input())

honey=list(map(int, input().split()))
psum=[0]*(N)
psum[0]=honey[0]
for i in range(1,N):
    psum[i]=psum[i-1]+honey[i]

res=0
for i in range(1, N-1):
    res=max(res, psum[N-1]-psum[0]-honey[i]+psum[N-1]-psum[i])

for i in range(1, N-1):
    res=max(res, psum[N-2]-honey[i]+psum[i-1])

for i in range(1, N-1):
    res=max(res, psum[N-1]-honey[0]-honey[N-1]+honey[i])

print(res)