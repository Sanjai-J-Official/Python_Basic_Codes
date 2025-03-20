s=input("Enter the String :")
new_s=''
for i in range(1,len(s)+1):
    
    new_s=new_s+ s[len(s)-i]

print(new_s)
