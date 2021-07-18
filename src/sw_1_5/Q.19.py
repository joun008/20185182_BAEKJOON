#1912번
import sys
input = sys.stdin.readline

N = int(input())
M = list(map(int,input().split()))
check_plus=0
check_minus=0
memo=[]
for k in range(N) :
    if M[k]>0 :
        check_plus+=M[k]
    else : 
        if check_plus!=0 :
            memo.append(check_plus)
            check_plus=0
        memo.append(M[k])

if check_minus!=0 :
    memo.append(check_minus)
if check_plus!=0:
    memo.append(check_plus)

length = len(memo)
nums = memo.index(max(memo))
Maximum = max(memo)
dp =[0]*(length)
dp[0]= memo[0]
result=dp[0]
#탐색A
if length==1 :
    print(dp[0])
    exit()
else :
    for k in range(1,length) :
        #아래와 코드 탐색을 다시 큰 수 부터 진행 할 수 있다
        dp[k] = max(dp[k-1]+memo[k],memo[k])
        result = max(result,dp[k])

print(result)
