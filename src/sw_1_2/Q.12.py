#1759
import sys
input = sys.stdin.readline
from itertools import combinations

N,M = map(int,input().split())
char = list(input().split())
mo = ["a","e","i","o","u"]
char.sort()
result = list(combinations(char,N))
time=0

for k in result :
    check = False
    time = N
    for j in k :
          if j in mo :
            time -= 1
            check = True

    if time>=2 and check==True :
        for j in k :
            print(j,end="")
        print()
