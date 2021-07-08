#10973번
N = int(input())
s = list(map(int,input().split()))
check = True
x=0
for i in range(N-1,0,-1) :
    if s[i-1] > s[i] :
        x=i-1
        break
T = sorted(s[x+1:],reverse=True)
print(T,s[x])
for i in range(len(T)):
    if s[x]>T[i]:
        check=False
        s[x],T[i]=T[i],s[x]
        s = s[:x+1]+T
        for k in s :
            print(k,end=" ")
        break

if check :
    print(-1)
