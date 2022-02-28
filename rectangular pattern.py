n=int(input())
k=n
for i in range(1,n+1):
    for j in range(0,i):
        print(k-j,end="")
    if n%2!=0:
        for s in range(n+2,2*i-1-1,-1):
            print(k-i+1,end="")
    else:
        for s in range(n * 2-2, 2 * i - 1, -1):
            print(k - i + 1, end="")
    for p in range(k-i+1,n+1):
        if p!=1:
            print(p,end="")
    print()
for i in range(1,n):
    for j in range(n,i,-1):
        print(j,end="")
    for s in range(0,2*i-1):
        print(i+1,end="")
    for p in range(i+1,n+1):
        print(p,end="")

    print()