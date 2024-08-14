m,n=map(int,input().split())
mat=[]
s=[]
for i in range(m):
    row=list(map(int,input().split()))
    mat.append(row)
    s.append(sum(row))
print(s)
