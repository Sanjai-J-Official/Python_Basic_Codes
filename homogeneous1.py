tup=(1,2,3,4,5,'6',2,2)
count=0
for i in tup:
    if type(tup[0])==type(i):
        count+=1
    else:
        break
print(count)