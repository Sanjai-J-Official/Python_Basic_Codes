'''n=int(input("Enter :"))
i=n
s=0
while i>0:
    ld=i%10
    s=s*10+ld
    
    i=i//10
if n==s:
    print("This is an Palindrome Number")
else:
    print("Not a palindrome")'''

n=int(input("Enter:"))
s=int(str(n)[::-1])
print("Palindrom") if s==n else print("Not palindrome")
