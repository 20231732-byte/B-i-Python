# Nhập 3 số nguyên
a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
c = int(input("Nhập số nguyên thứ ba: "))

# a) Tính tổng và tích
tong = a + b + c
tich = a * b * c

print("a) Tổng =", tong)
print("a) Tích =", tich)

# b) Hiệu của 2 số bất kỳ (ví dụ: a - b)
print("b) Hiệu (a - b) =", a - b)

# c) Phép chia của 2 số bất kỳ (ví dụ: a và b)
if b != 0:
    print("c) a // b (chia lấy nguyên) =", a // b)
    print("c) a % b (phần dư) =", a % b)
    print("c) a / b (kết quả chính xác) =", a / b)
else:
    print("c) Không thể chia cho 0")