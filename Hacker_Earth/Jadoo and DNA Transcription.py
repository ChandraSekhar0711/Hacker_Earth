x=input()
y=''
flag='T'
for i in x:
    if i not in ['G','C','A','T']:
        print('Invalid Input') 
        flag='F'
        break
    else:
            if i=='G':
                y+='C'
            elif i=='C':
               y+='G'
            elif i=='T':
                y+='A'
            elif i=='A':
                y+='U'
if flag=='T':
    print(y)
