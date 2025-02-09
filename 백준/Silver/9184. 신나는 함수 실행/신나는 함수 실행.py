import sys
input=sys.stdin.readline

dp=[[[0 for a in range(100)] for b in range(100)] for c in range(100)]
    
def w(a, b, c):     
    if a<=0 or b<=0 or c<=0:
        return 1
    elif a>20 or b>20 or c>20:
        return w(20, 20, 20)
    if dp[a][b][c]:
        dp[a][b][c]

    else:
        if c>b>a:
            dp[a][b][c]=w(a, b, c-1)+w(a, b-1, c-1)-w(a, b-1, c)
        else:
            dp[a][b][c]=w(a-1, b, c)+w(a-1, b-1, c)+w(a-1, b, c-1)-w(a-1, b-1, c-1)
    return dp[a][b][c]
        

while 1:
    a, b, c=list(map(int, input().split(" ")))
    if a==b==c==-1:
        break

    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")