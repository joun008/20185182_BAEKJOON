#2156번
N = int(input())
arr = []
rec = [0]*(10001)
for k in range(N) :
    arr.append(int(input()))

'''점화식
n번째 잔을 마셨을 때
-> n-1잔을 마시지 않았다
dp[n] = dp[n-2]+array[n]
-> n-1잔을 마셨다
dp[n] = dp[n-3]+array[n-1]+array[n]

but, 두잔을 연속 안 마시는 경우가 생김
dp[n]= max(dp[n-1],dp[n])
'''
if N==1 :
    print(arr[0])
elif N==2 :
    print(arr[0]+arr[1])
else :
    rec[0] = arr[0]
    rec[1] = arr[1]+arr[0]
    rec[2] = max(arr[0]+arr[1],arr[1]+arr[2],arr[0]+arr[2])
    for k in range(3,N) :
        rec[k] = max(rec[k-2]+arr[k],rec[k-3]+arr[k-1]+arr[k])
        rec[k] = max(rec[k-1],rec[k])

    print(rec[N-1])