#11057번
N = int(input())

back =[1]*10
arr = [0]*(1001)

for k in range(1,N+1) :
        total=0
        for j in range(10) :
            total += back[j]
        
        arr[k]=total%10007

        for j in range(9,0,-1) :
            for t in range(j) :
                back[j] += back[t]

print(arr[k])
