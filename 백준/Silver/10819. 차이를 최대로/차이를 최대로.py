import sys

input=sys.stdin.readline

N=int(input())

nums=list(map(int, input().split()))

used=[]
flag=[False]*N
def backtracking(used, tmpres, res):
    if len(used)==N:
        res.append(tmpres)
        return
    for i in range(N):
        if not flag[i]:
            used.append(nums[i])
            flag[i]=True
            if len(used)<2:
                backtracking(used, tmpres, res)
            else:
                backtracking(used, tmpres+abs(used[-1]-used[-2]), res)
            used.pop()
            flag[i]=False

res=[]
backtracking([], 0, res)
print(max(res))