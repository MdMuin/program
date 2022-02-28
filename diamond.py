m=int(input())
if m%2!=0:
    n=(m//2)+1
    l=m-n
i=1
while i<=n:
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j=1
    k=2*i-1
    while j<=k:
        print("*",end="")
        j=j+1
    print()
    i=i+1

i=l
while i>=1:
    s=l
    while s>=i:
        print(" ",end="")
        s=s-1
    j=1
    p=2*i-1
    while j<=p:
        print("*",end="")
        j=j+1
    print()
    i=i-1