"""num1=100
num2=990
 
lis=[]
while num1<num2:
    first_digit=num1//100
    center_digit=(num1//100)*10 - num1//10
    last_digit=num1%10
  
    if last_digit%5==0 or last_digit==0:
         if first_digit%2!=0 and center_digit%2!=0 and last_digit%2!=0:
            lis.append(num1)
    num1+=1
print(tuple(lis))"""

i=100

while i<=136:
    temp=i
    c=True
    while temp>0:
        id=temp%10
        print("id",id)
        if id%2==0:
            c=False
            break
        temp//=10
        print(temp)
    if c:
        if i%5==0 :
            print(i)
    i+=1

