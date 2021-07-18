#2225번
N,K = map(int,input().split())

memo = [[0]*(201) for _ in range(201)]
if K == 1:
    print(1)
    exit()
elif K == 2 :
    print(N+1)
    exit()
else :
    memo[1][N]=1
    for t in range(2,K+1) :
        result=0
        for j in range(N,-1,-1) :
            result+=memo[t-1][j]
            memo[t][j]=result

check=0
for j in range(0,N+1):
    check+=memo[K][j]
    check=check%1000000000

print(check)
