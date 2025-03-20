username='Admin'
password='admin123'

user=input("Enter the Username:")
passw=input("enter the password:")

if user==username:
    if passw==password:
        print("Welcome instagram>>>!")
    else:
        print(" incorrect password")
else:
    print("Incorrect Username")

    