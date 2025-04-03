import sys
input = sys.stdin.readline

S=input().rstrip()
T=input().rstrip()

while T:
    if T[-1]=="A":
        T=T[:-1]
    else:
        T=T[:-1][::-1]
    if T==S:
        print(1)
        sys.exit()
print(0)
