N = int(input())
arr = [int(input()) for _ in range(N)]
dp = [[0]*10 for _ in range(65)]
for k in range(10) :
    dp[1][k] =1

for j in range(2,65) :
    for p in range(9,-1,-1) :
        dp[j][p] = sum(dp[j-1][:p+1])

for k in arr :
    print(sum(dp[k]))