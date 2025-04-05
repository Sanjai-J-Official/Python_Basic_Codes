import random

i=0
score=0
while i<3:
    ren_num=random.randint(1,9)
    
    n=int(input("Enter the Number:"))

     
    if n==ren_num:
        score+=10
     
    i+=1
print(score)