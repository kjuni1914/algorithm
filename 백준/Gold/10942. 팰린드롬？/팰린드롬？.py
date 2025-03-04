import sys
sys.setrecursionlimit(10**6)

input=sys.stdin.readline

N=int(input())

nums=list(map(int, input().split()))
dp=[[True if i==j else None for i in range(N)] for j in range(N)]

def query(S, E):
    if dp[S][E] is not None:
        return dp[S][E]
    else:
        if nums[S]==nums[E]:
            if S+1<E-1:
                dp[S][E]=query(S+1, E-1)
            else:
                dp[S][E]=True
        else:
            dp[S][E]=False
    return dp[S][E]

for _ in range(int(input())):
    S, E=map(int, input().split())
    S, E=S-1, E-1
    print(int(query(S, E)))