def function():
    a=eval(input("Enter the Input:"))
    p=1
    for i in a:
        if type(i)==int:
            p*=i
    return p 
value=function()
print(value)