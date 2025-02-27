import sys
input=sys.stdin.readline

char=input().rstrip()

if len(char)>9:
    MAX=(len(char)-9)//2+9
else:
    MAX=len(char)

def backtracking(char, res, visited):
    if len(visited)==MAX:
        print(res)
        sys.exit()

    tmp=int(char[0])
    if tmp not in visited and 0<tmp<=MAX:
        visited.add(tmp)
        backtracking(char[1:], res+char[0]+" ", visited)
        visited.remove(tmp)
    tmp=int(char[0:2])
    if len(char)>=2 and 0<tmp<=MAX and tmp not in visited:
        visited.add(tmp)
        backtracking(char[2:], res+char[0:2]+" ", visited)
        visited.remove(tmp)

backtracking(char, "", set())