#11724 연결 요소 찾기
import sys
input =sys.stdin.readline
sys.setrecursionlimit(10000)
N,M = map(int,input().split())
arr = [[]for i in range(N+1)]
for i in range(M) :
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

visited = []
def dfs(start) :
    visited.append(start)
    for i in arr[start] :
        if i not in visited :
            dfs(i)
    return visited
count=0

for j in range(1,N+1) :
    if j not in visited : 
        count+=1
        dfs(j)
print(count)
