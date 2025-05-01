def func():
    inp=input("Enter:")
    count=0
    for i in inp:
        if 65<=ord(i)<=90:
            count+=1
    print(count)
func()