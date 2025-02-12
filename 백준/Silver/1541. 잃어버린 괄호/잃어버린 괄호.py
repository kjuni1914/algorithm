import sys

input=sys.stdin.readline

res=0
tmpres=0
tmp=0
minus=False
for i in input().strip():
    if minus:
        if i=="+":
            tmp+=tmpres
            tmpres=0
        elif i=="-":
            tmp+=tmpres
            tmpres=0
        else:
            tmpres*=10
            tmpres+=int(i)
            res-=tmp
            tmp=0
    else:
        if i=="+":
            res+=tmpres
            tmpres=0
        elif i=="-":
            minus=True
            res+=tmpres
            tmpres=0
        else:
            tmpres*=10
            tmpres+=int(i)
if minus:
    res-=tmpres
else:
    res+=tmpres

print(res)