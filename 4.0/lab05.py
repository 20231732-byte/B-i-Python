def bai5():
    # Tạo file mẫu
    with open("demo_file2.txt", "w", encoding="utf-8") as f:
        f.write("Dem so luong tu xuat hien abc abc abc 12 12 it it eaut")

    # Đọc file
    with open("demo_file2.txt", "r", encoding="utf-8") as f:
        text = f.read()

    # Tách từ
    words = text.split()

    # Đếm
    dem = {}
    for w in words:
        if w in dem:
            dem[w] += 1
        else:
            dem[w] = 1

    # In kết quả
    print("Kết quả:", dem)