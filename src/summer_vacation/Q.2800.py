from collections import deque

string = input()

result_string = deque([])
result_giho= deque([])
def solution(arr):
    giho = []
    for k in range(len(arr)) :
        if arr[k]=="(" :
            giho.append(k)

        elif arr[k]==")" :
            t = giho.pop()
            result_giho.append([t,k])
            result_string.append(arr)

solution(string)
fin_result=[]
for i in range(len(result_giho)-1,-1,-1) :
    count=0
    for j in range(i+1) :
        count+=1
        tx,ty = result_giho.popleft()
        string_ = result_string.popleft()
        new_string = string_[:tx]+string_[tx+1:ty]+string_[ty+1:]
        if count<=i:
            solution(new_string)
        fin_result.append(new_string)
        print(result_giho)
        print(result_string)
fin_result.sort()
for k in fin_result :
    print(k)
