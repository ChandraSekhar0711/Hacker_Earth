n=int(input())
rem=n
for i in range (0,n):
    if rem>i:
        rem=rem-i
    else:
        print("patlu")
        break
    if rem>i:
        rem=rem-(i*2)
    else:
        print("motu")
        break
