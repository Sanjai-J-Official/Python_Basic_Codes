import datetime 
a=datetime.datetime.now()
time=a.strftime('%H')

food_time=input("Enter the name:")
foods=[['Dosa','idly','pongal','upma'],['briyani','sambar','chicken rice','mutton briyani'],['porota','egg rice','chapadi','lemon rice']]
if food_time==time:
    for i in range(len(foods[0])):
        print(foods[0][i])
    n=int(input(""))
elif food_time==time:
    print("""""")