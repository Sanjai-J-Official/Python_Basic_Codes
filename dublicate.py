n=list((1,2,3,2,1,2,5,10))

li=[]
i=0

while i<len(n):
    if n[i] not in li:
        li.append(n[i])
    i+=1
print(tuple(li))

