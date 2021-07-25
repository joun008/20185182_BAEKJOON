N = int(input())
arr = list(map(int,input().split()))
dp=[0]*(N+1)
if N==1 :
    print(arr[0])
    exit()
elif N==2 :
    print(max(arr[0]*2,arr[1]))
    exit()
else :
    dp[1] = arr[0]
    for k in range(2,N+1) :
        for j in range(k) :
            dp[k] = max(arr[k-j-1]+dp[j],dp[k])

print(dp[N])