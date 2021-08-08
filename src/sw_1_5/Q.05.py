import sys
input = sys.stdin.readline

dp = [i for i in range(1000001)]
dp[0] = 1
for i in range(3,1000001) :
    dp[i] = (dp[i-1]+dp[i-2]+dp[i-3])%1000000009

N = int(input())
for k in range(N) :
    n = int(input())
    print(dp[n]%1000000009)