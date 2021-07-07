def num(k) :
    if k==1 : return 1
    if k==2 : return 2
    if k==3 : return 4
    return num(k-1)+num(k-2)+num(k-3)

N = int(input())
for i in range(N) :
    M = int(input())
    print(num(M))
