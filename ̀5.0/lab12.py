n = int(input("Nhập độ dài n: "))

_list = ['abc', 'xyz', 'aba', '1221', 'ii', 'ii2', '5yhy5']

dem = 0

for x in _list:
    if len(x) >= n and x[0] == x[-1]:
        dem += 1

print("Kết quả:", dem)