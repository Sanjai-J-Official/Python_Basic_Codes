n=input("Enter the string:")
a=n.split()
print(len(a))
 
c={}
d={}
e={
}
f={}
print(a[0][0])
i=0
while i<len(a):
    c[a[i]]=len(a[i])
    d[a[i]]=a[i][::-1]
    e[a[i]]=a[i][::2]
    j=0
    st=''
    while j<len(a[i]):
        if a[i][j] not in "aeiouAEIOU":
            
            st+=a[i][j]
        j+=1
    f[a[i]]=st
    i+=1
print(c,d,e,f,sep="\n")