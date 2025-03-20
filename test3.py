#whether char is vewol or consonent
 
n=input("Enter the Char:")
if 'a'<= n <='z' or 'A'<=n <='Z':
    if n in 'aeiouAEIOU':
        print(f"{n} is Vewols")

    else:
            
        print(f"{n} is Consonent")

