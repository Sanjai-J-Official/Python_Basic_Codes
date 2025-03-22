txt=input("Enter the String:")
i=0
count=0
first_char=txt[0]
 
while i<len(txt):
    if txt[i] in first_char:
        count+=1
    i+=1
print(count)

