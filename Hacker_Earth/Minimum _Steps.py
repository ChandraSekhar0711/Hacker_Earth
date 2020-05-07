T=int(input("enter no of inputs...:"))
count1=0
count=0
for i in range(T):
        k,m,n=map(int,input().split())
        while True:
                if k==m:
                        break
                elif k<m:
                        k=k*n
                        count=count+1
                elif k>m:
                        k=k-2
                        count=count+1
                        if k==m:
                                break
                        else:
                                k=k-1
                                count=count+1
                        
                                        
        count1=count-count1
        print(count1)
                                        
                                
                                
                
