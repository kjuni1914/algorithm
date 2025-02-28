import sys

input=sys.stdin.readline

N=int(input())+1
ASC=[i for i in range(10)]
DESC=[9-i for i in range(10)]
cmd=input().rstrip().split()

def backtracking(used, res, nums):
    if len(res)==N:
        print(res)
        return True

    if cmd[len(res)-1]=="<":
        for i in range(len(nums)):
            if nums[i] not in used and nums[i]>int(res[-1]):
                used.append(nums[i])
                if backtracking(used, res+str(nums[i]), nums):
                    return True
                used.pop()
    else:
        for i in range(len(nums)):
            if nums[i] not in used and nums[i]<int(res[-1]):
                used.append(nums[i])
                if backtracking(used, res+str(nums[i]), nums):
                    return True
                used.pop()
    return False

for i in range(len(ASC)):
    if backtracking([DESC[i]], str(DESC[i]), DESC):
        break

for i in range(len(ASC)):
    if backtracking([ASC[i]], str(ASC[i]), ASC):
        break
