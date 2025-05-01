#wap FIND SIMPLE INTREST USING TYPE 3
#SI=(PTR)/100
 
def func():
    P=int(input("enter amount :"))
    T=int(input("Enter Time in Month:"))
    R=float(input("Enter rate of intrest:"))
    SI=(P*T*R)/100
    return SI
print(func())