#write a program extract all the lower case alphabet from the giver string
st='pyThOJKSjhhdSJjHgTHmI'

length=len(st)
i=0
while i<length:
     
    if ord(st[i])>=97 and ord(st[i])<=122:
        print(st[i])
    
    i+=1