#1748번
N = int(input())
M = len(str(N))
nums=0
for k in range(M-1,-1,-1) :
    nums+=(N-10**k+1)*(k+1)
    N-=(N-10**k+1)

print(nums)
