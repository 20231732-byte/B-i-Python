n = int(input("Nhập số nguyên dương: "))
a = 0
tong = 0

while a <= n:
    if a % 2 == 0:
        tong = tong + a
    a = a + 1  # luôn tăng a

print("Tổng các số chẵn từ 0 đến", n, "là:", tong)