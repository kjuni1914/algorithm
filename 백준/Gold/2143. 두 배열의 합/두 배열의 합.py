import sys
input=sys.stdin.readline

T=int(input())

n=int(input())
A=list(map(int, input().split()))
m=int(input())
B=list(map(int, input().split()))

dpA=[0]*(n+1)
for i in range(len(A)):
    dpA[i+1]=dpA[i]+A[i]

dpB=[0]*(m+1)
for i in range(len(B)):
    dpB[i+1]=dpB[i]+B[i]

Apos={}
for i in range(len(dpA)):
    for j in range(i):
        if dpA[i]-dpA[j] not in Apos:
            Apos[dpA[i]-dpA[j]]=1
        else:
            Apos[dpA[i]-dpA[j]]+=1

ans=0
for i in range(len(dpB)):
    for j in range(i):
        if T-(dpB[i]-dpB[j]) in Apos:
            ans+=Apos[T-(dpB[i]-dpB[j])]

print(ans)