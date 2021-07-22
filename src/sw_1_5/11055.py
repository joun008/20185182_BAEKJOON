N = int(input())
arr = list(map(int,input().split()))
dp = [0]*(1000)
 
for k in range(N) :
    dp[k]=arr[k]
    for j in range(k) :
        if arr[k]>arr[j] :
            dp[k] = max(dp[j]+arr[k],dp[k])

print(max(dp[:N]))