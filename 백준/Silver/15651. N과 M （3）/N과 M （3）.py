import sys

input=sys.stdin.readline

N, M=map(int, input().split())

def backtracking(path, visited=[False]*N, res=[]):
    if len(path)==M:
        res.append(" ".join(path))
        return

    for i in range(N):
        path.append(nums[i])
        backtracking(path)
        path.pop()
    return res

nums=[str(i+1) for i in range(N)]

res=backtracking([])

for i in res:
    print(i)