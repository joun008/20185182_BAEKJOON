#6603번 조합 사용해서 풀이
import sys
input = sys.stdin.readline
from itertools import combinations
while True:
    M = list(map(int,input().split()))
    if M[0]==0 :
        break
    items =[ i+1 for i in range(M[0])]
    combi = combinations(items,6)
    for j in list(combi) :
        for k in j :
            print(M[k],end=" ")
        print()
    print()
    
#dfs 사용해 백트래킹한 문제
def dfs(start, depth):
    if depth == 6:
        for i in range(6):
            print(combi[i], end=' ')
        print()
        return
    for i in range(start, len(s)):
        combi[depth] = s[i]
        dfs(i + 1, depth + 1)
combi = [0 for i in range(13)]
while True:
    s = list(map(int, input().split()))
    if s[0] == 0:
        break
    del s[0]
    dfs(0, 0)
    print()
