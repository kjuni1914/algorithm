import sys

input=sys.stdin.readline

N, S=map(int, input().split())

nums=list(map(int, input().split()))
cnt=0

def recursion(tmpsum, idx):
    global cnt
    if idx==N:
        if tmpsum==S:
            cnt+=1
        return
    
    recursion(tmpsum+nums[idx], idx+1)
    recursion(tmpsum, idx+1)

recursion(0, 0)
if S==0:
    cnt-=1
print(cnt)