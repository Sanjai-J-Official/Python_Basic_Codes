n=eval(input("Enter the Input:"))

if type(n)==list:
    
    if type(n[0])==str:
        
        if n[0][0] in 'aeiouAEIOU':
            if len(n[0])%2==1:
                mid=len(n[0])//2 
                print("middle value:",n[0][mid])  
            else:
                print("String:",n[0])                 
        else:
            print("Starting Letter Not Vowels")
    else:
        print("Not String")
else:
    print("Not List")