#'python is easy'
#{'python':'pythn','is:'s','easy':'sy'}

txt='python is easy'.split()
d={}
for i in txt:  
    st=''
    for j in i:   
        if j not in 'AEIOUaeiou':
            st+=j
    d[i]=st
print(d) 