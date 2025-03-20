a=input("Enter the word:")

data=[]
for i in range(len(a)):
     
    for j in a[i]:
        
        if j in a: 
            m=a.count(f'{j}')
            letter=f"{j} count of :{m}"
        data.append(letter)    
            
    
datas=[]   
 


for j in range(len(data)):
    if data[j][-1]=='1':
        datas.append(data[j]) 
    else:
        if data[j] in datas:
            continue
        else:
            datas.append(data[j])
  
            
for i in sorted(datas):
    print(i)
       
 
    