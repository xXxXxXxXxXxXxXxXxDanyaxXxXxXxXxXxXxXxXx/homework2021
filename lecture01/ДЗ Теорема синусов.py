import math 
A = float(input("������� ������� � "))
B = float(input("������� ������ � "))
alpha = float(input("������� ���� alpha "))
L = (A**2+B**2-2*A*B*math.cos(math.radians(alpha)) )**0.5
print(L)
    
