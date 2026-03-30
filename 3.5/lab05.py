import math

# Nhập hệ số
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

# Kiểm tra
if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        print("Phương trình có nghiệm x =", -c / b)
else:
    delta = b**2 - 4*a*c
    
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("Phương trình có 2 nghiệm:", x1, "và", x2)
    elif delta == 0:
        x = -b / (2*a)
        print("Phương trình có nghiệm kép:", x)
    else:
        print("Phương trình vô nghiệm")