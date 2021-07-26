stack_alpha=[]
stack_giho=[]

line = input()
line_list=[]

line_list.append("(")
for k in line:
    line_list.append(k)
line_list.append(')')

for k in line_list :
    if k=='(' :
        stack_giho.append('(')
    elif k==')' :
        temp_giho_multi=[]
        temp_giho_sum=[]
        temp_alpha_sum=[]
        temp_alpha_multi=[]
        while True :
            P=stack_giho.pop()
            if P=="(" :
                break
            elif P=="+" or P=="-" :
                temp_giho_sum.append(P)
                temp_alpha_sum.append(stack_alpha.pop())
            else :
                temp_giho_multi.append(P)
                temp_alpha_multi.append(stack_alpha.pop())
            
        temp_alpha_sum.append(stack_alpha.pop())
        temp_alpha_multi.append(temp_alpha_sum.pop(0))
        for k in range(len(temp_giho_multi)) :
            A = temp_alpha_multi.pop()
            B = temp_alpha_multi.pop()
            C = temp_giho_multi.pop()
            sol = A+B+C
            temp_alpha_multi.append(sol)
        
        if len(temp_alpha_multi)!=0 :
            temp_alpha_sum.insert(0,temp_alpha_multi.pop())
        for k in range(len(temp_giho_sum)) :
            A = temp_alpha_sum.pop()
            B = temp_alpha_sum.pop()
            C = temp_giho_sum.pop()
            sol = A+B+C
            temp_alpha_sum.append(sol)
        stack_alpha.append(temp_alpha_sum.pop())

    elif k == '+' or k=='-':
        checking = False
        new_giho=[]
        new_alpha=[]
        while True :
            if stack_giho[len(stack_giho)-1]=='*' or stack_giho[len(stack_giho)-1]=='/' :
                checking =True    
                new_giho.append(stack_giho.pop())
                new_alpha.append(stack_alpha.pop())
            else :
                break
        if checking :
            new_alpha.append(stack_alpha.pop())
            for t in range(len(new_giho)) :
                A = new_alpha.pop()
                B = new_alpha.pop()
                C = new_giho.pop()
                sol = A+B+C
                new_alpha.append(sol)
            stack_alpha.append(new_alpha.pop())
        stack_giho.append(k)
    elif k=='*' or k=='/' :
        stack_giho.append(k)
    else :
        stack_alpha.append(k)

for j in stack_alpha :
    print(j)