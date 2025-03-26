n='abcd123456ab'
num=[1,2,3,4,5,2,1,2,4,1,7]
s=""
num_n=[]
i=0
while i<len(n):
   
    if n[i] not in s:
        s+=n[i]
    
    i+=1
j=0
while j<len(num):
     
    if num[j] not in num_n:
        num_n.append(num[j])
    
    j+=1



print(num_n)
print(s)