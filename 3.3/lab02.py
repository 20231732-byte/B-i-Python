# Nhập 3 số nguyên dương
a = int(input("Nhập cạnh a: "))
b = int(input("Nhập cạnh b: "))
c = int(input("Nhập cạnh c: "))

# Kiểm tra điều kiện tam giác
if a + b > c and a + c > b and b + c > a:
    print("Đây là độ dài ba cạnh của một tam giác")
else:
    print("Đây không phải là ba cạnh của một tam giác")