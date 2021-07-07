#10819번 - 직관적 풀이
import sys
import math
input = sys.stdin.readline

N = int(input())
M = list(map(int,input().split()))

M.sort(reverse=True)
k =len(M)-1
total=0

for i in range(len(M)//2) :
    if i == 0 :
        total += M[0]*2 - M[k]- M[k-1]
    elif i == len(M)//2-1 :
        total += M[i] - M[k-i+1]
    else :
        total += M[i]*2 - M[k-i+1] - M[k-i-1]

if len(M)%2==1 and len(M)>3:
    t = len(M)//2
    if M[t-1]-M[t]>M[t]-M[t+1] :
        total += M[t-1]-M[t]
    else :
        total += M[t]-M[t+1]
print(total)

#permutations 
from itertools import permutations
import sys

n = int(sys.stdin.readline())
arr = permutations(list(map(int, sys.stdin.readline().split())))
ans = 0
for a in arr :
  sums = 0
  for i in range(n-1) :
    sums += abs(a[i]-a[i+1])
  ans = max(ans,sums)
print(ans)
