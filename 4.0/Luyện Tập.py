import math

# 1. Hàm tính tổng 2 số
def tong_2_so(a, b):
    return a + b

# 2. Hàm tính tổng nhiều số
def tong_n_so():
    n = int(input("Nhập số lượng phần tử: "))
    tong = 0
    for i in range(n):
        x = int(input(f"Nhập số thứ {i+1}: "))
        tong += x
    return tong

# 3. Hàm kiểm tra số nguyên tố
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# 4. Tìm số nguyên tố trong [a, b]
def tim_nguyen_to(a, b):
    for i in range(a, b + 1):
        if la_so_nguyen_to(i):
            print(i, end=" ")
    print()

# 5. Hàm kiểm tra số hoàn hảo
def la_so_hoan_hao(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n

# 6. Tìm số hoàn hảo trong [a, b]
def tim_hoan_hao(a, b):
    for i in range(a, b + 1):
        if la_so_hoan_hao(i):
            print(i, end=" ")
    print()

# ===== MENU =====
while True:
    print("\n===== MENU =====")
    print("1. Tính tổng 2 số")
    print("2. Tính tổng n số")
    print("3. Kiểm tra số nguyên tố")
    print("4. Tìm số nguyên tố trong [a, b]")
    print("5. Kiểm tra số hoàn hảo")
    print("6. Tìm số hoàn hảo trong [a, b]")
    print("0. Thoát")

    chon = int(input("Chọn chức năng: "))

    if chon == 1:
        a = int(input("Nhập a: "))
        b = int(input("Nhập b: "))
        print("Tổng =", tong_2_so(a, b))

    elif chon == 2:
        print("Tổng =", tong_n_so())

    elif chon == 3:
        n = int(input("Nhập số: "))
        if la_so_nguyen_to(n):
            print("Là số nguyên tố")
        else:
            print("Không phải số nguyên tố")

    elif chon == 4:
        a = int(input("Nhập a: "))
        b = int(input("Nhập b: "))
        print("Các số nguyên tố:")
        tim_nguyen_to(a, b)

    elif chon == 5:
        n = int(input("Nhập số: "))
        if la_so_hoan_hao(n):
            print("Là số hoàn hảo")
        else:
            print("Không phải số hoàn hảo")

    elif chon == 6:
        a = int(input("Nhập a: "))
        b = int(input("Nhập b: "))
        print("Các số hoàn hảo:")
        tim_hoan_hao(a, b)

    elif chon == 0:
        print("Thoát chương trình")
        break

    else:
        print("Chọn sai, nhập lại!")