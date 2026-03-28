import time

# Lấy năm hiện tại
x = time.localtime()
year = x[0]

# Nhập năm sinh
nam_sinh = int(input("Nhập năm sinh: "))

# Tính tuổi
tuoi = year - nam_sinh

# In kết quả
print("Tuổi của bạn là:", tuoi)