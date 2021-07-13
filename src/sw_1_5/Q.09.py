#10844번
N = int(input())

arr =[0]*(101)
back1 = [1]*(10)
back2 = [0]*(10)
back1[0] = 0
for k in range(1,N+1) :
    if k==1 :
        arr[k]=9
    else :
        arr[k]=(arr[k-1]*2 -back1[0]-back1[9])%1000000000
        check1 = back1[1]
        check2 = back1[8]
        for j in range(1,9) :
            back2[j] = back1[j-1]+back1[j+1]
        back2[0] = check1
        back2[9] = check2
        for k in range(0,10) :
            back1[k] = back2[k]
        
        
print(arr[N])
