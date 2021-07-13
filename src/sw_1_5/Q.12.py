#9465번

N = int(input())
'''
앞에 부터 가능한 모든 경우에서 최대한을 구하면 된다.
50 10 100 20 40
30 50 70  10 60
일 경우를 보면
50 40  MAX(100,30)+100 
30 100 MAX(40,50)+70
아래와 같이 계속 하면 됨
'''
for i in range(N) :
    M = int(input())
    arr = [list(map(int,input().split())) for i in range(2)]
    arr[0][1] +=arr[1][0]
    arr[1][1] +=arr[0][0]
    for k in range(2,M) :
        #핵심 코드!
        arr[0][k] +=max(arr[1][k-1],arr[1][k-2])
        arr[1][k] +=max(arr[0][k-1],arr[0][k-2])
    
    print(max(arr[0][M-1],arr[1][M-1]))
