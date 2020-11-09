num = int(input("Введите количество элементов: "))
sequence = 1
res = 0
for i in range(num):
    res += sequence
    sequence *= -0.5
print(f"Сумма = {res}")