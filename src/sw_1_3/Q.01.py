#백준 15649
import sys
input =sys.stdin.readline
from itertools import permutations
N,M = map(int,input().split())
nums = [i+1 for i in range(N)]

K = list(permutations(nums,M))
for i in K :
    for j in i :
        print(j,end=" ")
    print()
