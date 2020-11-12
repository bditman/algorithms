start = 2
end = 99
num_start = 2
num_end = 9
for i in range(num_start, num_end + 1):
    res = 0
    for j in range(start, end + 1):
        if j % i == 0:
            res += 1
    print(f"Есть {res} чисел, кратных {i} в диапазоне от {start} до {end}")