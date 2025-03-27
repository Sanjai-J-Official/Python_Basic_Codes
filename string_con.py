s=input().split()
i=0
dicts={}
while i<len(s):
    st=''
    j=0
    while j<len(s[i]):
        st+=chr(ord(s[i][j])-32)
        j+=1

    dicts[s[i]]=st
    i+=1
print(dicts)