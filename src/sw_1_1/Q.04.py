N = int(input())
def gcd(M,N) :
    if M%N==0:
        return N
    else :
        return gcd(N,M%N)

for i in range(N) :
    num = list(map(int,input().split()))
    num = num[1:]
    num.sort()
    sum=0
    for j in range(len(num)-1) :
        for k in range(j+1,len(num)) :
            sum+= gcd(num[k],num[j])
    print(sum)
