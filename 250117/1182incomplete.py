import sys

input=sys.stdin.readline

N, K=map(int, input().split(" "))
num=list(map(int, input().split(" ")))
summation=[0]

res=0
for i in num:
    for j in range(len(summation)):
        summation.append(summation[j]+i)


print(summation)
print(summation.count(K)-1)