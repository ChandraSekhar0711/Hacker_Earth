n=int(input())
for i in range(n):
    x,y,a,b=map(int,input().split())
    if (x*y==a+b):
        print("Yes")
    else:
        print("No")
