#14226번
import sys
input = sys.stdin.readline
from collections import deque
S = int(input())

arr = [[-1] *(1001) for _ in range(2001)]
#arr[화면에 나온 이모티콘 개수][클립보드 이모티콘 갯수]
#클리보드에 상관없이 화면에 나온 이모티콘의 개수중 작은거
def bfs(S) :
    queue = deque([[1,0]])
    arr[1][0] = 0
    while queue :
        T = queue.popleft()
        row = T[0]
        col = T[1]
        #1번 과정
        if arr[row][row] == -1 :
            arr[row][row] = arr[row][col]+1
            queue.append([row,row])

        #2번 과정
        if row+col<=S and arr[row+col][col] == -1 :
            arr[row+col][col] = arr[row][col]+1
            queue.append([row+col,col])
        
        #3번 과정
        if row-1>=0 and arr[row-1][col]==-1 :
            arr[row-1][col] =arr[row][col]+1
            queue.append([row-1,col])


bfs(S)
r = arr[S][1]
for k in range(2,1001) :
    if arr[S][k] !=-1 :
        r = min(r,arr[S][k])

print(r)
