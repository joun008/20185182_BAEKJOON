N = int(input())
arr = list(map(int,input().split()))
dp = [1]*(N)
dp_list=[[]*(N) for j in range(N)]
dp_list[0].append(arr[0])
for k in range(1,N) :
    hint=-1
    for j in range(k,-1,-1) :
        if arr[k]>arr[j] :
            if dp[j]+1>dp[k] :
                hint=j
            dp[k]=max(dp[j]+1,dp[k])
    if hint!=-1 :
        dp_list[k].extend(dp_list[hint])
    dp_list[k].append(arr[k])

max=0
check=0
count=-1
for k in dp_list:
    count+=1
    if max<len(k) :
        max=len(k)
        check=count
print(max)
for j in dp_list[check] :
    print(j,end=" ")