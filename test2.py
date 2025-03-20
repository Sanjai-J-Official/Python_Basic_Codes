#wriet check wether data is list or not ,if its is list then check wiether is 1st value str or not   if its is palindrome or not 
#if palinromo print str else: reverse 
lists=['malayalam',12,20]

#palinrome easy list[0][::-1]


if type(lists)==list:
    if type(lists[0])==str:
        st='' 
        for i in range(len(lists[0])-1,-1,-1):
            st=st+lists[0][i]
        if st == lists:
            print("this is palindrome")
        else:
            print(st)                    
    else:
        print("This is not string")
else:

    print("not list")
