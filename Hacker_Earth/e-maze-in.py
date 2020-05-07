s=input("")
x=0
y=0
for i in s:
    if i=='L':
        x,y=x-1,y
    elif i=='R':
        x,y=x+1,y
    elif i=='U':
        x,y=x,y+1
    elif i=='D':
        x,y=x,y-1
print(x,y)    
