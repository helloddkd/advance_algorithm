import sys
sys.stdin = open('2117.txt', 'r')

def dfs(x,y,k) :
    global n,m,home,result
    dfsresult = 0
    dfsmoney = k*k+(k-1)*(k-1)
    for i,j in home :
        if abs(x-i) + abs(y-j) < k :
            dfsresult += 1
    if dfsmoney <= dfsresult*m :
        if result < dfsresult :
            result = dfsresult
    if k <= n :
        dfs(x,y,k+1) #결국 n+1까지 봄
for a in range(int(input())) :
    n,m = list(map(int,input().split()))
    item = [list(map(int,input().split())) for i in range(n)]
    result = 0
    home = []
    for j, y in enumerate(item) :
        for i, x in enumerate(y) :
            if item[j][i] > 0 :
                home.append((i,j))
    for i in range(n) :
        for j in range(n) :
            dfs(i,j,1)
    print('#{} {}'.format(a+1, result))