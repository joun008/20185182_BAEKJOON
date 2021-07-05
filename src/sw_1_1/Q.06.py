import sys
N = 10000000 #이 숫자 이상으로 해야 index error 안뜸
check = [False for _ in range(N)]
for i in range(2,int(N**0.5)) :
    if check[i]==False :
        for j in range(i*2,N,i) :
            check[j] = True
prime_number = [i for i,j in enumerate(check) if i>2 and j==False]
count=0
while True :
    N = int(sys.stdin.readline())
    count+=1
    if count>100000 :
        break
    checking = True
    if N == 0 :
        break
    for i in prime_number :
        t = N-i
        if t<0:
            break
        if check[t] == False :
            checking = False
            print("%d = %d + %d"%(N,i,t))
            break
        if checking == False :
            break
    if checking :
        print("Goldbach's conjectrue is wrong.")
