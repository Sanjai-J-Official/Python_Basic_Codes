n=int(input("Enter the input:"))

temp=n
i=temp
sum=0
while i>0:
    ld=i%10
    fact=1
    j=ld
    while j>0:
        fact=fact*j
        j-=1
    sum+=fact
    i//=10
print(sum,n) 


