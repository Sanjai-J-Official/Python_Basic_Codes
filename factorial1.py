#check factorial of a number
#check given number is prime number or not 

n=int(input("Enter :"))
i=n
fact=1
while i>0:
    fact=fact*i
    i-=1
print(fact)
