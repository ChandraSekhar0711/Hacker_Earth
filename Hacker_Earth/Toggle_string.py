S=input("")
x=""
for i in S:
    if i.isupper():
        x=x+(i.lower())
        
    elif i.islower():
        x=x+(i.upper())
print(x)
