import sys
input=sys.stdin.readline

N, M=map(int, input().split())

nums=list(map(int, input().split()))

nums.sort()

print(nums[M-1])