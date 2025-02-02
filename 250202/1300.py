import sys

input=sys.stdin.readline

N=int(input())
k=int(input())

st=0
end=N**2

while st<=end:
    mid=(st+end)//2
    tmp=0
    for i in range(1, N+1):
        tmp+=min(N, mid//i)
    if tmp>=k:
        res=mid
        end=mid-1
    else:
        st=mid+1

print(res)