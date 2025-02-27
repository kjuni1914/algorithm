import sys
input=sys.stdin.readline

char=input().rstrip()

if len(char)>9:
    MAX=(len(char)-9)//2+9
else:
    MAX=len(char)
nums=[i+1 for i in range(MAX)]

def backtracking(char, res, visited):
    if len(visited)==MAX:
        print(res)
        sys.exit()

    for i in range(len(nums)):
        if nums[i] not in visited:
            if str(nums[i])==char[0]:
                visited.add(nums[i])
                backtracking(char[1:], res+str(nums[i])+" ", visited)
                visited.remove(nums[i])

            elif str(nums[i])==char[0:2]:
                visited.add(nums[i])
                backtracking(char[2:], res+str(nums[i])+" ", visited)
                visited.remove(nums[i])

print(backtracking(char, "", set()))