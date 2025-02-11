import sys

input=sys.stdin.readline

N=int(input())

people=list(map(int, input().split()))
res=[]

for i in range(len(people)-1, -1, -1):
    res.insert(people[i], str(i+1))

print(" ".join(res))