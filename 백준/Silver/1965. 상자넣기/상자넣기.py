import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
nums=list(map(int, input().split()))
dp=[1]*1001
for i in nums:
    dp[i]=max(dp[0:i])+1

print(max(dp)-1)