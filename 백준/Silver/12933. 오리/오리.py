import sys

input=sys.stdin.readline

sound=input().rstrip()

if len(sound)%5!=0:
    print(-1)
    sys.exit()

qcnt=0
ucnt=0
acnt=0
ccnt=0
kcnt=0
res=0
for i in range(len(sound)):
    if sound[i]=="q":
        qcnt+=1
    elif sound[i]=="u":
        ucnt+=1
    elif sound[i]=="a":
        acnt+=1
    elif sound[i]=="c":
        ccnt+=1
    else:
        kcnt+=1

    if qcnt<ucnt or ucnt<acnt or acnt<ccnt or ccnt<kcnt:
        print(-1)
        sys.exit()
    res=max(qcnt-kcnt, res)

if qcnt==kcnt:
    print(res)
else:
    print(-1)