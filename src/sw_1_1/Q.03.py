N = int(input())
def gcd(M,N) :
    if M%N==0:
        return N
    else :
        return gcd(N,M%N)

for i in range(N) :
    M, K = map(int,input().split())
    if M > K :
        result = gcd(M,K)
        print((M*K)//result)
    else :
        result = gcd(K,M)
        print((M*K)//result)
