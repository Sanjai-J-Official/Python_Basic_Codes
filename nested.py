age=int(input("Enter the age:"))
day=input('Enter the day:')

weekday=['monday','tuesday','wednesday','thursday','friday']
weekend=['saturday','sunday']

if age<5:
    print("Free ticket")
elif age >= 5 and age<= 18:
    if day in weekend:
        print("Ticket Price :150")
    else:
        print("Ticket Price :100")
else:
    if day in weekend:
        print("Ticket Price :250")
    else:
        print("Ticket Price :200")

