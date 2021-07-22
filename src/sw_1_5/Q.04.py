N = int(input())
arr = [int(input()) for _ in range(N)]

for k in arr :
    dp=[0]*(k+1)
    if k==1 :
        print(1)
        continue
    elif k==2 :
        print(2)
        continue
    elif k==3 :
        print(4)
        continue
    else :
        dp[1]=1
        dp[2]=2
        dp[3]=4
        for t in range(4,k+1) :
            dp[t]=dp[t-1]+dp[t-2]+dp[t-3]
        print(dp[k])

'''
N = int(input())
dp = [i for in range(20)]
dp[0] = 0
for k in range(3,len(dp)) :
    dp[k]=dp[k-1]+dp[k-2]+dp[k-3]

for j in range(N) :
    M = int(input())
    print(dp[M])
'''