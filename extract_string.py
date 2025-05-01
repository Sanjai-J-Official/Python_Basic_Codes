txt='This is Python123 @gamil.com'
vowels='' 
consonants=''
special=''
for i in txt:
    if 'A'<=i<='Z' or 'a'<=i<='z':
        if i not in 'AEIOUaeiou':
            consonants+=i
        else:
            vowels+=i
    elif '0'<=i<='9':
        pass
    else:
        special+=i
print(vowels,consonants,special,sep='\n')