#11726번
import sys
input = sys.stdin.readline

#F(N)=F(N-1)+F(N-2)
N = int(input())

arr =[0]*(1001)
for k in range (1,1001) :
    if k==1 :
        arr[k]=1
    elif k==2 :
        arr[k]=2
    else :
        arr[k]=(arr[k-1]+arr[k-2])%10007
    
print(arr[N])
