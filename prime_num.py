'''
n=int(input("Enter the input:"))

if n<2:
    print("its not a prime number")
else:
    i=2
    while n>i:
        if n%i==0:
            print("its not a prime number")
            break
        i+=1
    else:
        print("Prime Number")
'''

n=int(input("Enter:"))

if n%2==0 or n%3==0 or n%5==0:
    print("not prime")
else:
    print("prime") 