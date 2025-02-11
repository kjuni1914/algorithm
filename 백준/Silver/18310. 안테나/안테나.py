import sys
import math
input=sys.stdin.readline

N=int(input())

houses=list(map(int, input().split()))

houses.sort()

print(houses[math.ceil(len(houses)/2)-1])