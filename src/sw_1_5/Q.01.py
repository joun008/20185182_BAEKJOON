#1463번
#점화식 arr(N) = min(arr[N//3]+1,arr[N//2]+1,arr[i-1]+1)
import sys
input = sys.stdin.readline

N = int(input())

arr = [0]*(N+1)
arr[1] = 0

for i in range(2,N+1) :
    arr[i] = arr[i-1]+1

    if i%2==0 and arr[i]>arr[i//2]+1:
        arr[i] = arr[i//2]+1

    if i%3==0 and arr[i]>arr[i//3]+1:
        arr[i] = arr[i//3]+1

print(arr[N])
