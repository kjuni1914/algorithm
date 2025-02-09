import sys

i = int(sys.stdin.readline())
stack = []
for _ in range(i):
    tmp = sys.stdin.readline()
    cmd = tmp.split()[0]
    if cmd == "push":
        num = int(tmp.split()[1])
        stack.append(num)
    elif cmd == "top":
        if len(stack) != 0:
            print(stack[len(stack)-1])
        else:
            print(-1)
    elif cmd == "empty":
        if len(stack) != 0:
            print(0)
        else:
            print(1)
    elif cmd == "pop":
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
    else:
        print(len(stack))