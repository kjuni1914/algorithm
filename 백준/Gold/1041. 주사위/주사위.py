import sys

input=sys.stdin.readline
N=int(input())

dice=list(map(int, input().split()))
if N>1:
    candidate3=[]
    for i in dice[2], dice[3]:
        for j in [dice[0]+dice[1], dice[1]+dice[5], dice[0]+dice[4], dice[4]+dice[5]]:
            candidate3.append(i+j)

    candidate2=[]
    for i in dice[0], dice[1], dice[4], dice[5]:
        for j in dice[2], dice[3]:
            candidate2.append(i+j)
    candidate2.extend([dice[0]+dice[1], dice[1]+dice[5], dice[0]+dice[4], dice[4]+dice[5]])

    dice.sort()
    candidate2.sort()
    candidate3.sort()

    print(candidate3[0]*4+candidate2[0]*(8*N-12)+dice[0]*((N-2)**2*5+(N-2)*4))
else:
    dice.sort()
    print(sum(dice[:5]))