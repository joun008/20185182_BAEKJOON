import itertools
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
num = [i for i in range(N)]
public = list(itertools.combinations(num,(N//2)))
length = len(public)
maximun = 1000000
for k in range(length//2) :
    num1=num2=0
    public2 = itertools.permutations(public[k],2)
    public3 = itertools.permutations(public[length-k-1],2)
    for j in public2 :
        num1 += arr[j[0]][j[1]]

    for t in public3 :
        num2 += arr[t[0]][t[1]]

    maximun = min(maximun,abs(num1-num2))

print(maximun)