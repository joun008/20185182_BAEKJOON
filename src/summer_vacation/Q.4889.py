check=0
while True :
    check+=1
    N = input()
    galho=[]
    for k in range(len(N)) :
        if len(galho)==0 :
            galho.append(N[k])
        else:
            if N[k]=="{" :
                galho.append(N[k])
            elif N[k]=="}":
                if galho[-1]=="{":
                    galho.pop()
                else :
                    galho.append(N[k])
            elif N[k]=="-" :
                exit()
    result=0
    while True :
        if len(galho)==0 :
            break
        current1 = galho.pop()
        current2 = galho.pop()
        if current1=="{" and current2=="}" :
            result+=2
        else :
            result+=1

    print("{}. {}".format(check,result))