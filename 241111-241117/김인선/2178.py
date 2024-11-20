# [BOJ-Silver1] 2178_미로 탐색
from collections import deque


n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(x,y):
   queue = deque() 
   queue.append((x,y))

   while queue:
       x,y = queue.popleft()

       for i in range(4):
           nx = x + dx[i]
           ny = y + dy[i]

           if (0 <= nx < n and 0 <= ny < m) and graph[nx][ny] == 1:
               queue.append((nx, ny))
               graph[nx][ny] = graph[x][y] + 1
               
   return graph[n-1][m-1]

print(bfs(0,0))