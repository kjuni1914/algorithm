import sys
import heapq

input=sys.stdin.readline

array=[]
room=[]

for i in range(int(input())):
    array.append(tuple(map(int, input().split())))

array.sort(key=lambda x:(x[0]))

for i in array:
    if room and room[0]<=i[0]:
        heapq.heappop(room)
    heapq.heappush(room, i[1])

print(len(room))