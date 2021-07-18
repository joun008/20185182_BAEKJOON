#메모리 초과로 다시 풀어야됨 1107번
import itertools
N = int(input())
M = int(input())
if M != 0 : 
    arr = list(map(int,input().split()))
else :
    arr=[]
use =[]
for k in range(10) :
    if k not in arr :
        use.append(k)

length =len(str(N))
oh = list(itertools.product(use,repeat=length))
oh2 = list(itertools.product(use,repeat=length-1))
oh3 = list(itertools.product(use,repeat=length+1))
if length<=1 :
    oh+=oh3
else :
    oh+=oh3
    oh+=oh2

checking=False
result=10000000
for j in oh :
    check=0
    for k in j :
        check*=10
        check+=k
    if result >= abs(check-N)+len(str(check)) :
        result = abs(check-N)+len(str(check))
        checking =True

if checking==False :
    print(abs(N-100))
else :
    hi = min(abs(N-100),result)
    print(hi)
