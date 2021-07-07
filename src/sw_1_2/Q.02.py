E,S,M = map(int,input().split())
E-=1
S-=1
M-=1
check = S
while True :
    if check % 15 == E and check % 19 ==M :
        print(check+1)
        break
    else :
        check += 28
