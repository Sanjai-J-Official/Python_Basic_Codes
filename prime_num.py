ran=200
it= 100
lis=[]
while it<ran:
    n=it
    if n<2:
        continue#print("its not a prime number")
    else:
        i=2
        while n>i:
            if n%i==0:
                #print("its not a prime number")
                break
            i+=1
        else:
            lis.append(n)
            #print("Prime Number")
    it+=1
print(lis)
'''

n=int(input("Enter:"))

if n%2==0 or n%3==0 or n%4==0 or n%5==0:
    print("not prime")
else:
    print("prime") '''      

