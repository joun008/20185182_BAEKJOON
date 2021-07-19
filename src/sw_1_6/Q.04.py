#2529
'''
nums.append()하고 재귀돌리고 nums.pop()을 하는 이유 재사용을 위해
그렇게 사용한다.
'''
N = int(input())
arr = list(input().split())
visited =[False]*10
nums=[]
result=[]

def solve(count,pre) :
    if count == N+1 :
        result.append("".join(map(str,nums)))
        return
    
    for i in range(10) :
        if arr[count-1]=='<' and pre<i and not visited[i] :
            visited[i]=True
            nums.append(i)
            solve(count+1,i)
            nums.pop()
            visited[i] = False
        elif arr[count-1]=='>' and pre>i and not visited[i] :
            visited[i]=True
            nums.append(i)
            solve(count+1,i)
            nums.pop()
            visited[i] = False

for i in range(10) :
    visited[i]=True
    nums.append(i)
    solve(1,i)
    nums.pop()
    visited[i]=False

print(result[-1])
print(result[0])