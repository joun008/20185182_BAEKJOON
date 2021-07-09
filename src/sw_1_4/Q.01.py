import sys
input = sys.stdin.readline

N,M = map(int,input().split())
result=[[]for i in range(N)]
visited = [False] * N
for i in range(M) :
    st,end =map(int,input().split())
    result[st].append(end)
    result[end].append(st)

def dfs(idx,number) :
    if number ==4:
        print(1)
        exit()
    for i in result[idx]:
        if not visited[i] :
            visited[i] = True
            dfs(i,number+1)
            visited[i] = False 

#다시 돌아갈 수도 있기 때문에 False로 해야됨 아니면 답이 다름 예를 들면
5 5
0 1
1 3
1 2
2 3
3 4
# 일반적인 알고리즘으로 해결 못함

for i in range(N) :
    visited[i] = True
    dfs(i,0)
    visited[i] =False
#여기서도 False로 해야 한다 왜냐면 새로운 visited를 만들지 않기 때문에 재사용하기 위해서!!
print(0)
