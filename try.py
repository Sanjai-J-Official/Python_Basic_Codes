#wat p the key value pairs from a dictionary where key should be belong single value datatype 
# and value belong to immutable datatype 

inp={1:'python',2:'erere','er':343}#eval(input("Enter the Dictionary:"))
d={}
# for i in inp:
#     if type(i) in [int ,float,complex]:
#         if type(inp[i]) not in [list,set,dict]:
#             d[i]=inp[i]
# print(d)
i=len(inp)-1  #3
m=0
items=list(inp.items())

while i>=m:
    if type(items[i][0]) in [int,float,complex]:
        if type(items[i][1]) not in [list,set,dict]:
            d[items[i]]=items[i][1]  
    i-=1
print(d)
