// 내 풀이
N = 9
num=[]
# num = sorted(int(input() for i in range(9))
for i in range(N) :
    M = int(input())
    num.append(M)

num.sort()
def swap(array,i,j) :
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

recent = sum(num[:7])
total = 100
if recent == total :
    for i in range(7) :
        print(num[i])
else :
    total -= recent
    list1=[]
    list2=[]
    check = True
    for i in range(7) :
        list1.append(num[7]-num[i])
        list2.append(num[8]-num[i])
        if total == list1[i]  :
            check = False
            swap(num,i,7)
            break
        elif total == list2[i] :
            check = False
            swap(num,i,8)
            break

    if check :
        for k in range(7) :
            for j in range(7) :
                if total == list1[k] + list2[j] :
                    check = False
                    swap(num,k,7)
                    swap(num,j,8)
                    break
            if check == False :
                break
    result = num[:7]
    result.sort()
    for i in range(7):
        print(result[i])

//최적화 풀이
l=sorted(int(input())for i in range(9))
for i in l:
 for j in l:
  if i+j==sum(l)-100:
    l.remove(i);
    l.remove(j);
    break
for i in l:
  print(i)
