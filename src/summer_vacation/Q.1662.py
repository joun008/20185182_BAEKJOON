M = input()
num = []
N=[]
#리스트에 담기
for k in range(len(M)) :
    N.append(M[k])

#괄호 앞에 있는 수를 제외한 모든 숫자는 1로 변경
for k in range(len(N)-1) :
    if N[k]=='(' or N[k]==')' :
        continue
    else :
        if N[k+1]=="(" :
            continue
        else :
            N[k] = 1

if N[len(N)-1]!="(" and N[len(N)-1]!=")" :
    N[len(N)-1]=1


#핵심코드
for k in range(len(N)) :
    check=0
    if N[k]==")" :
        while True :
            number = num.pop()
            if number=="(":
                break
            else :
                check += number
        number = num.pop()
        check = int(number)*check
        num.append(check)
    else :
        num.append(N[k])

#최종답안
result=0
while True :
    if len(num)==0:
        break
    else :
        result+=num.pop()
print(result)