'''
xr
0 => (0,0)
1 => (0, 1), (1, 0)
2 => (0,2), (1,1), (2, 0)

2n-2 => (n-1, n-1)
r+c = i


xc
0 => (n-1, 0)
1 => (n-2, 0), (n-1, 1)
2 => (n-3, 0), (n-2, 1), (n-1, 2)

2n-2 => (0, n - 1)
c-r+n-1 = i
'''
def rcConverter(r,c):
    return r+c, c-r+n-1

def rcInverseConverter(xr, xc):
    return (xr-xc+n-1)//2, (xr+xc-n+1)//2

def btPass(xr, xc, b):
    r, c = rcInverseConverter(xr, xc)
    if xr == 2*n-2 or xr == 2*n-3 and (c == n-1 or b):
        return -1, -1
    
    if b or r == 0 or c == n-1:
        c += 2
        while r != n-1 and c != 0 :
            r += 1
            c -= 1
    else :
        r -= 1
        c += 1
    return r, c

def bt(r, c, cnt) :
    xr, xc = rcConverter(r, c)
    tmp = 0
    if board[r][c] and not(positionxr[xr] or positionxc[xc]) :
        nr, nc = btPass(xr, xc, True)
        if nr == nc == -1 :
            return cnt + 1
        positionxr[xr] = True
        positionxc[xc] = True
        tmp = bt(nr, nc, cnt+1)
        positionxr[xr] = False
        positionxc[xc] = False
    
    nr, nc = btPass(xr, xc, False)
    if nr == nc == -1 :
        return cnt 
    cnt = max(tmp, bt(nr, nc, cnt))
    return cnt

n = int(input())

board = [list(map(int,input().split())) for _ in range(n)]
positionxr = [False]*(2*n-1)
positionxc = [False]*(2*n-1)

if n == 1 :
    print(int(board[0][0]))
    exit()

ans = 0
for i in range(2):
    ans += bt(i,0,0)

print(ans)