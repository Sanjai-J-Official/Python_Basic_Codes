txt='This is python'
inp=input("Enter the char:")
st=''
for i in txt:
    if i==inp:
        print(f'found the char: {i}')
        break 
    st+=i
    print(st)
    #print(f'seaching string.....{inp}')
