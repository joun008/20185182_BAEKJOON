#11053번

N = int(input())
arr = list(map(int,input().split()))
dp = [1]*(1000) 
for k in range(N) :
    for j in range(k) :
        if arr[k]>arr[j] :
            dp[k] = max(dp[j]+1,dp[k])

#핵심 끝 점이 가장 안 클 수도 있음  
print(max(dp[:N+1]))