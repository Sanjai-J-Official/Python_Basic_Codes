def function(a):
    sum=0
    for i in a:
        if type(i) in [int,float,complex]:
            sum+=i
    
    print(sum)
inp=eval(input("Enter:"))
function(inp)

