import sys

input=sys.stdin.readline

N, M=map(int, input().split(" "))
num=list(map(int, input().split(" ")))

s, e=0, 0
tmpSum=0
res=0
while e<=N-1:
    while e<=N-1:
        tmpSum+=num[e]
        e+=1
        if tmpSum>=M:
            break
    while tmpSum-num[s]>=M and s<=e:
        tmpSum-=num[s]
        s+=1
    if tmpSum>=M and (res==0 or res>e-s):
        res=e-s

print(res)