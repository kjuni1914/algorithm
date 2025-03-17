import sys

input=sys.stdin.readline
N=int(input())

used=set()
for _ in range(N):
    cmd=input().rstrip()
    separate=list(cmd.split())
    res=""
    flag=True
    for i in separate:
        if flag and i[0].upper() not in used:
            used.add(i[0].upper())
            flag=False
            res+="["+i[0]+"]"+i[1:]
        else:
            res+=i
        res+=" "
    res=res[:len(res)-1]
    if flag:
        res=""
        for i in range(len(cmd)):
            if flag and cmd[i].upper() not in used and cmd[i]!=" ":
                used.add(cmd[i].upper())
                flag=False
                res+="["+cmd[i]+"]"
            else:
                res+=cmd[i]
    print(res)