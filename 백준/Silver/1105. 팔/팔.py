import sys

input=sys.stdin.readline

L, R=input().rstrip().split()

cnt=0
i=0
if len(L)!=len(R):
    print(0)
else:
    while i<len(L) and L[i]==R[i]:
        if L[i]=="8":
            cnt+=1
        i+=1
    print(cnt)