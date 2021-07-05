N = int(input())
M = list(map(int,input().split()))
count=0
for i in M :
    check = True
    if i == 1 :
        continue
    for j in range(2,i):
        if i%j==0 :
            check = False
            break
    if check==True :
        count+=1
print(count)
