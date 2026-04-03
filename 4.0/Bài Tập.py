# ===== B1: Đọc n dòng đầu của file =====
def doc_n_dong():
    ten_file = input("Nhập tên file: ")
    n = int(input("Nhập số dòng cần đọc: "))
    
    with open(ten_file, "r", encoding="utf-8") as f:
        for i in range(n):
            line = f.readline()
            if not line:
                break
            print(line.strip())

# ===== B2: Ghi và đọc file =====
def ghi_va_doc():
    ten_file = input("Nhập tên file: ")
    
    # Ghi file
    with open(ten_file, "w", encoding="utf-8") as f:
        text = input("Nhập nội dung: ")
        f.write(text)
    
    # Đọc lại
    with open(ten_file, "r", encoding="utf-8") as f:
        print("Nội dung file:")
        print(f.read())

# ===== B3 =====
def bai3():
    ten_file = "demo_file1.txt"
    
    # Tạo file
    with open(ten_file, "w", encoding="utf-8") as f:
        f.write("Thuc\nhanh\nvoi\nfile\nIO\n")
    
    # a) In trên 1 dòng
    with open(ten_file, "r", encoding="utf-8") as f:
        content = f.read().replace("\n", " ")
        print("a) In trên 1 dòng:")
        print(content)
    
    # b) In từng dòng
    with open(ten_file, "r", encoding="utf-8") as f:
        print("b) In từng dòng:")
        for line in f:
            print(line.strip())

# ===== MENU =====
while True:
    print("\n===== MENU =====")
    print("1. Đọc n dòng đầu file")
    print("2. Ghi và đọc file")
    print("3. Bài 3")
    print("0. Thoát")

    chon = int(input("Chọn: "))

    if chon == 1:
        doc_n_dong()
    elif chon == 2:
        ghi_va_doc()
    elif chon == 3:
        bai3()
    elif chon == 0:
        print("Thoát!")
        break
    else:
        print("Chọn sai!")