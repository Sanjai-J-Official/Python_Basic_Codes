 #arguments  *args  all the single values its mean all the single values it can be use
    #for positional arguments,it is also called tuple packing because tuple is the default data type 
    #which is imutable in nature 
    #in tuple packing user can pass n number of values but it will treated as single arguments 
    #in the function call 
def func(*a):
    for i in a:
        print(i)
b=[10,20]
c=[20,23]
func(b,c)