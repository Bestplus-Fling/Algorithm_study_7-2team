from collections import deque
def dfs(idx, path): #path 폐업 시키지않을 치킨집
    if len(path) == m:
        global min_val
        min_val = min(min_val, bfs(path))
        return
    if m - len(path) > len(chickens) - idx:
        return
    path.append(idx)
    dfs(idx + 1, path)
    path.pop()
    dfs(idx + 1, path)

def bfs(path):
    dis = 0
    for home in homes:
        x, y = home
        c_dis = float('inf')
        for idx, chicken in enumerate(chickens):
            if idx in path:
                cx, cy = chicken
                c_dis = min(c_dis,abs(x - cx) + abs(y - cy))
        dis += c_dis
    return dis


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dxl = [0, 1, 0, -1]
dyl = [1, 0, -1, 0]
chickens = []
homes = []
min_val = float('inf')
for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            chickens.append((i, j))
        elif arr[i][j] ==  1:
            homes.append((i, j))

dfs(0, [])
print(min_val)