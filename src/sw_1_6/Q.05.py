#1339
N = int(input())
arr=[]
for k in range(N) :
    M = input()
    arr.append(M)
count_alpha=0
# 65=A and 90=Z
visited_alpha = [0]*(36)
for j in arr :
    for k in range(len(j)) :
        if visited_alpha[ord(j[k])-65]==0 :
            visited_alpha[ord(j[k])-65]=1
            count_alpha+=1

print(count_alpha)

visited_num =[0]*(10)
num=[]
sol=[]
len
maximun=0
for k in range(N) :
    maxinum = max(10,len(arr[k]))

def solve(count) :

    if count==count_alpha :
        sol.append("".join(map(str,num))