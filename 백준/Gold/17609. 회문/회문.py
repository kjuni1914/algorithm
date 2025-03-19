import sys
sys.setrecursionlimit(10**5)

input=sys.stdin.readline

def judge(S, st, end, coin):
    if st>=end:
        return True

    if S[st]!=S[end]:
        if coin[0]:
            coin[0]=False
            return judge(S, st+1, end, coin) or judge(S, st, end-1, coin)
        else:
            return False
    else:
        return judge(S, st+1, end-1, coin)

for _ in range(int(input())):
    S=input().rstrip()
    coin=[True]
    if judge(S, 0, len(S)-1, coin):
        if coin[0]:
            print(0)
        else:
            print(1)
    else:
        print(2)