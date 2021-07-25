n,k = map(int,input().split())
arr = [int(input()) for _ in range(n)]
dp=[0]*(k+1)
dp[0]=1
arr.sort(reverse=True)
for coin in arr :
    for j in range(1,k+1) :
        if j-coin<0 :
            continue
        dp[j] +=dp[j-coin]
    print(dp)