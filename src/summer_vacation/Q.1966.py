from collections import deque
import sys
input = sys.stdin.readline
case = int(input())
for k in range(case) :
    print_num=[]
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    queue = deque([])

    #순서 부여
    for p in range(len(arr)) :
        queue.append([arr[p],p])
    
    while True :
        #탈출 조건
        if len(arr)==1 :
            t= queue.popleft()
            print_num.append(t[1])
            break
        # 크기 비교 조건
        if arr[0]<max(arr[1:]) :
            t = arr.pop(0)
            arr.append(t)
            ma = queue.popleft()
            queue.append(ma)
        else :
            t = queue.popleft()
            arr.pop(0)
            print_num.append(t[1])

    print(print_num.index(M)+1)
    
