#1260번
import sys
input= sys.stdin.readline
N,M,V = map(int,input().split())
arr = [[]for i in range(N+1)]
for i in range(M) :
    a,b= map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

#dfs 재귀함수로 구현
visited=[]
def dfs(start) :
    visited.append(start)
    arr[start].sort()
    for i in arr[start]:
        if i not in visited :
            dfs(i)
    return visited
for k in dfs(V) :
    print(k,end=" ")

print()
#bfs queue으로 구현
visited=[]
def bfs(start) :
    visited.append(start)
    queue = [start]
    while queue :
        v = queue.pop(0)
        arr[v].sort()
        for w in arr[v]:
            if w not in visited :
                visited.append(w)
                queue.append(w)
                
    return visited

for k in bfs(V) :
    print(k,end=" ")

print()
#dfs stack으로 구현
visited= []
def dfs1(start) :
    stack = [start]
    while stack :
        v = stack.pop()    
        if v not in visited :
            visited.append(v)
            T = sorted(arr[v],reverse=True)
            stack.extend(T)
    
    return visited

for k in dfs1(V) :
    print(k,end=" ")
