#2193번
N = int(input())

arr = [0]*(91)
check =[0]*2 
for k in range(N+1) :
    if k==1 :
        arr[k]=1
        check[1]=1
    else :
        arr[k] = check[0]*2+check[1]
        temp = check[0]
        check[0] = check[0]+check[1]
        check[1] = temp


print(arr[N])
