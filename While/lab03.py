# Nhập số dương
n = int(input("Nhập số nguyên dương: "))

# Kiểm tra điều kiện số dương
while n <= 0:
    n = int(input("Nhập lại số nguyên dương: "))

# Kiểm tra số nguyên tố
if n < 2:
    print(n, "không phải là số nguyên tố")
else:
    i = 2
    is_prime = True
    
    while i <= n // 2:
        if n % i == 0:
            is_prime = False
            break
        i += 1
    
    if is_prime:
        print(n, "là số nguyên tố")
    else:
        print(n, "không phải là số nguyên tố")