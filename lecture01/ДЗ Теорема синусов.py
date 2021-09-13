import math 
A = float(input("Введите сторону А "))
B = float(input("Введите строну В "))
alpha = float(input("Введите угол alpha "))
L = (A**2+B**2-2*A*B*math.cos(math.radians(alpha)) )**0.5
print(L)
    
