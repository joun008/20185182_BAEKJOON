N = int(input())
s = list(map(int,input().split()))
check = True
x=0
for i in range(N-1,0,-1) :
    if s[i-1] < s[i] :
        x=i-1
        break
for i in range(N-1,0,-1):
    if s[x]<s[i]:
        check=False
        s[x],s[i]=s[i],s[x]
        s=s[:x+1]+sorted(s[x+1:])
        for k in range(N) :
            print(s[k],end=" ")
        break
if check :
    print(-1)
