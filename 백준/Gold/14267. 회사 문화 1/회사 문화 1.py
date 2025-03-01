import sys
sys.setrecursionlimit(10**5)

input=sys.stdin.readline

N, M=map(int, input().split())

boss=list(map(int, input().split()))
boss=[i-1 for i in boss]
compliment=[0 for _ in range(N)]
res=[None]*N

def dfs_sum(idx):
    if boss[idx]==-2:
        res[idx]=compliment[idx]
        return res[idx]

    if res[idx] is None:
        res[idx] = dfs_sum(boss[idx])+compliment[idx]

    return res[idx]

for _ in range(M):
    target, w=map(int, input().split())
    compliment[target-1]+=w

for i in range(N):
    dfs_sum(i)
    print(str(res[i]), end=" ")