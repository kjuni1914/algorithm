import sys

input=sys.stdin.readline

cmd=input().split(" ")

fsee = set()
fhear = set()

for i in range(int(cmd[0])):
    fsee.add(input().strip())

for i in range(int(cmd[1])):
    fhear.add(input().strip())

print(len(fsee & fhear))
for i in (sorted(fsee & fhear)):
    print(i)