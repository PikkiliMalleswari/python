n=int(input())
sum=0
for i in str(n):
    sum=sum+int(i)**len(str(n))
if(n==sum):
    print("armstrong")
else:
    print("not")
