
n=input("Enter:")
 
i=0
while i<len(n):
    if n.count(n[i])==1:
        print(n[i])
        break
    i+=1

 
