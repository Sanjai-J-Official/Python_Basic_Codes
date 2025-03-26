n=eval(input("Enter the list:"))

sum=0
fact=1
for i in range(len(n)):
    sum+=n[i]
    fact*=n[i]

print(f"sum :{sum} and factorial: {fact}")



