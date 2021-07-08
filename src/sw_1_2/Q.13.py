#1182번
import sys
input =sys.stdin.readline
N,S = map(int,input().split())
nums = list(map(int,input().split()))

subsets = [[]]

for num in nums :
    size = len(subsets)
    for y in range(size) :
        subsets.append(subsets[y]+[num])

count=0
del subsets[0]
for k in subsets :
    if sum(k)==S :
        count+=1

print(count)
