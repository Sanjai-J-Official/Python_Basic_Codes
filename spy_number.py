n=123
i=0
sum=0
mul=1
while n>i:
    ld=n%10
    sum=sum+ld
    mul=mul*ld
    n=n//10
print(sum,mul)
