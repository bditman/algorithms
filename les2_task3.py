num = input("Введите число, которые нужноо перевернуть: ")
res = ''
for i in num:
    res = i + res
print(f"Перевернутое значение = {res}")