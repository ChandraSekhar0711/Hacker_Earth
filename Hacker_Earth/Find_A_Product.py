n=int(input())
a=list(map(int,input().split()))

answer=1   
for i in range(0,n):
    answer=(answer*a[i])%(1000000007)
print(answer)
