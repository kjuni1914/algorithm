i = int(input())
res = 0
for _ in range(i):
    flag = True
    tmp = input()
    checker = set()
    tmp2 = ""
    for j in tmp:
        if tmp2 != j:
            if j in checker: 
                flag = False
            checker.add(j)
            tmp2 = j
    if flag:
        res+=1
print(res)