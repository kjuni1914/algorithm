import sys

input=sys.stdin.readline

N, M=map(int, input().split())

def backtracking(nums, visited, path, j, res=[]):
    if len(path)==M:
        res.append(" ".join(path))
    
    for i in range(j, N):
        if not visited[i]:
            visited[i]=True
            path.append(nums[i])
            backtracking(nums, visited, path, i)
            visited[i]=False
            path.pop()
    
    return res

nums=[str(i+1) for i in range(N)]
res=backtracking(nums, [False]*len(nums), [], 0)

for i in res:
    print(i)