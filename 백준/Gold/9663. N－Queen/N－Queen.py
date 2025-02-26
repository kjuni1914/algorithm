import sys

input=sys.stdin.readline

N=int(input())

cols=[False]*N
ru=[False]*(2*N-1)
rd=[False]*(2*N-1)

def backtracking(x, y):
    res=0
    if x==N-1:
        return 1
    for i in range(N):
        if cols[i] or ru[N-1+x+1-i] or rd[x+1+i]:
            continue
        else:
            cols[i]=True
            ru[N-1+x+1-i]=True
            rd[x+1+i]=True
            res+=backtracking(x+1, i)
            cols[i]=False
            ru[N-1+x+1-i]=False
            rd[x+1+i]=False
    return res

res=0
for i in range(N//2):
    cols[i]=True
    ru[N-1-i]=True
    rd[i]=True
    res+=backtracking(0, i)
    cols[i]=False
    ru[N-1-i]=False
    rd[i]=False
res*=2
if N%2==1:
    cols[N//2]=True
    ru[N-1-N//2]=True
    rd[N//2]=True
    res+=backtracking(0, N//2)
    cols[N//2]=False
    ru[N-1-N//2]=False
    rd[N//2]=False
print(res)