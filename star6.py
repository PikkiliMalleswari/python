n=5
for i in range(n):
    for j in range(n):
        if(j==0 or (j==0 and i>=n//2) or i==0 or i==n-1 or i==n//2 or i==n-1 or(j==n-1 and i>=n//2)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
