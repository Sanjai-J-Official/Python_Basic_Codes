num1=100
num2=400
lis=[]
while num1<num2:
    last_digit=num1%10
    first_digit=num1//100
    center_digit=(num1//100)*10 - num1//10
   ## print("first:",first_digit)
   # print("center:",center_digit)
    #print("last:",last_digit)
     
    if first_digit%2==0 and center_digit%2==0 and last_digit%2==0:
        lis.append(num1)
    num1+=1
print(tuple(lis))