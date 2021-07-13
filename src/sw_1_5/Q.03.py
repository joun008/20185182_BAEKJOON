#9095번

import sys
input =sys.stdin.readline
# F(N)=F(N-1)+F(N-2)+F(N-3)
N = int(input())

for k in range(N) :
    M = int(input())
    arr = [0]*(M+1)

    for k in range(1,M+1) :
        if k==1 :
            arr[k]=1
        elif k==2 :
            arr[k]=2
        elif k==3 :
            arr[k]=4
        else :
            arr[k]=arr[k-1]+arr[k-2]+arr[k-3]

    print(arr[M])
