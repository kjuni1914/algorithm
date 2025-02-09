import math

def solution(r1, r2):
    answer = 0
    tmp = 0
    answer = inner(r2) - innerWoutBorder(r1)
    return answer

def inner(r2):
    y = r2 - 1
    answer = 0
    for x in range(1, math.floor(r2 / 2**(1/2))+1):
        while x**2 + y**2 > r2**2:
            y-=1
        answer+=y-x
    answer *= 8
    answer += 4*(r2)
    answer += 4*(math.floor(r2 / 2**(1/2)))
    
    return answer

def innerWoutBorder(r2):
    y = r2 - 1
    answer = 0
    for x in range(1, math.floor(r2 / 2**(1/2))+1):
        while x**2 + y**2 >= r2**2:
            y-=1
        answer+=y-x
    answer *= 8
    answer += 4*(r2-1)
    answer += 4*(math.floor((r2-0.01) / 2**(1/2)))
    
    return answer