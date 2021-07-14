#1699번
N = int(input())
arr =[i for i in range(N+1)]

for k in range(4,N+1) :
    for j in range(1,int(k**(1/2))+1) :
        if arr[k]>arr[k-j*j]+1 :
            arr[k]=arr[k-j*j]+1

print(arr[N])
