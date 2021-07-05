M,N = map(int,input().split())
def gcd(M,N) :
    if M%N==0 :
        return N
    else :
        return gcd(N,M%N)

if M>N :
    answer = gcd(M,N)
    print(answer)
    print(M*(N//answer))
else :
    answer = gcd(N,M)
    print(answer)
    print(M*(N//answer))
