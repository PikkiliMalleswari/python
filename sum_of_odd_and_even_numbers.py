#a = int(input())
arr=list(map(int,input().split()))
even_sum=0
odd_sum=0
for i in arr:
    if i%2==0:
        even_sum+=i
    else:
        odd_sum+=i
print("odd.sum:",odd_sum)
print("even.sum:",even_sum)
