import random

print(random.random())
print(random.randint(1,999898))

name=['SANJAI',"PYTHON","JAVA","C++"]
weights=[10,5,2.5,1]
print(random.choices(name,weights=weights,k=3))