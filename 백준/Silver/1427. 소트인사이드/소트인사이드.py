import sys

input=sys.stdin.readline

l=" ".join(input()).split(" ")
l.pop()
l.sort(reverse=True)
print("".join(l))