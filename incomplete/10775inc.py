import sys

input=sys.stdin.readline

G=int(input())
P=int(input())

gate=[0]*(G+1)
ans=0
flag=True
for i in range(P):
    airplain=int(input())
    while 1:
        if gate[airplain]==0 and flag:
            gate[airplain]=1
            ans+=1
            break
        airplain-=1
        if airplain==0:
            flag=False
            break

print(ans)