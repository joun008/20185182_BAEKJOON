#2667번
N = int(input())
arr = [list(map(int,input())) for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
num=-1
def dfs(x,y,check) :
    global num
    if arr[x][y] == 1:
        num+=1
        arr[x][y]=check
    for k in range(4) :
        nx = x+dx[k]
        ny = y+dy[k]
        if nx<=-1 or ny>=N or nx>=N or ny<=-1:
            continue
        if arr[nx][ny] == 1 :
            arr[nx][ny] = check
            num+=1
            dfs(nx,ny,check)
#문제에서 가장 중요한 부분 global 변수 설정하기!!
    
number =2
number_list=[]
for k in range(N) :
    for j in range(N):
        if arr[k][j]==1 :
            num=0
            dfs(k,j,number)
            number+=1
            number_list.append(num)
            

number_list.sort()
print(number-2)
for k in number_list :
    print(k)
