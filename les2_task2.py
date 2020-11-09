num = input("Введиче число в котором нужно посчитать цифры: ")
even = 0
not_even = 0
for i in num:
    if int(i) % 2 == 0:
        even += 1
    else:
        not_even += 1
print(f"Количество четных цифр = {even}, нечетных = {not_even}")
