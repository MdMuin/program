m=int(input())
if m%2!=0:
    n=m//2
    j=0
    for i in range(0,n+1):
        for k in range(1,m+1):
            print(j*m+k,end=" ")
        print()
        j=j+2
    p=m-2
    for i in range(m-2,n-1,-1):
        for j in range(1,m+1):
            print(p * m + j, end=" ")
        print()
        p=p-2
else:
    n=m//2
    k=0
    for i in range(1,n+1):
        for j in range(1,m+1):
            print(k*m+j,end=" ")
        print()
        k=k+2
    p=m-1
    for i in range(n,0,-1):
        for j in range(1,m+1):
            print(p*m+j,end=" ")
        print()
        p=p-2


