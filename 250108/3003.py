import sys
input=sys.stdin.readline

ori = [1, 1, 2, 2, 2, 8]
cmd = list(map(int, input().split(" ")))
res = ""

for i, j in zip(ori, cmd):
    res+=str(i-j) + " "

print(res)
