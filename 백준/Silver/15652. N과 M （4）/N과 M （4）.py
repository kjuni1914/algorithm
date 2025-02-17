import sys

input=sys.stdin.readline
N, M=map(int, input().split())

def backtracking(path, st, res=[]):
    if len(path)==M:
        res.append(" ".join(path))
        return

    for i in range(st, N):
        path.append(nums[i])
        backtracking(path, i)
        path.pop()


    return res

nums=[str(i+1) for i in range(N)]

res=backtracking([], 0)

for i in res:
    print(i)