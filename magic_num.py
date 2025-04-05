n=int(input("Enter:"))
i=n
num=0
first=0
while i>0:
    ld=i%10
    num+=ld
    i//=10
    if i//10==0:
        first+=i

num2=0    
if num>=10:
    while num>0:
        ld=num%10
        num2+=ld
        num//=10
        
    print(num2)
else:
    print(num)
if first==num2:
    print(f"Magic the Number :{n}")
else:
    print("Not")
