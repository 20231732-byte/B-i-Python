# Bảng mã
bang_ma = {'a':'!', 'b':'@', 'c':'#', 'd':'$'}

# Tạo bảng giải mã (đảo key-value)
giai_ma = {}
for k, v in bang_ma.items():
    giai_ma[v] = k

# ===== Mã hóa =====
def ma_hoa(text):
    kq = ""
    for ch in text:
        if ch in bang_ma:
            kq += bang_ma[ch]
        else:
            kq += ch
    return kq

# ===== Giải mã =====
def giai_ma_text(text):
    kq = ""
    for ch in text:
        if ch in giai_ma:
            kq += giai_ma[ch]
        else:
            kq += ch
    return kq

# ===== TEST =====
text = input("Nhập chuỗi: ")

ma = ma_hoa(text)
print("Mã hóa:", ma)

giai = giai_ma_text(ma)
print("Giải mã:", giai)