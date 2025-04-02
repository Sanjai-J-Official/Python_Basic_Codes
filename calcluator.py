class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        print(f"Sum of {self.a} & {self.b} : {self.a + self.b } ")

    def sub(self):
        print(f'Sub of {self.a} & {self.b} : {self.a - self.b } ')

    def mul(self):  
        print(f'mul of {self.a} & {self.b} : {self.a * self.b } ')

    def div(self):
        if self.b==0:
            print("Second Operands is Zero So Cannot Divided")
        else:
            print(f'div of {self.a} & {self.b} : {self.a // self.b } ')
while True:
    print("""
    1)SUM
    2)SUB
    3)MULTIPLE
    4)DIVIDED
    5)Exit
    """) 
    n=int(input("Choose the Option:"))
    
    calc=Calculator(int(input("Enter the Num 1:")),int(input("Enter the Num 2:")))
    if n==1:
        calc.sum()
    elif n==2:  
        calc.sub()
    elif n==3:
        calc.mul()
    elif n==4:
        calc.div()
    else:
        break
    