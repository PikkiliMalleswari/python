n=int(input())
ar=list(map(int,input().split()))
for i in range(n):
    c=0
    for j in range(i,n):
        if(ar[i]==ar[j]):
            c+=1
    if c==2:
        print(ar[i])
