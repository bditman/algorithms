import random

size = 10
min = 0
max = 20
list = [random.randint(min, max) for _ in range(size)]
print(list)

min_num = 0
max_num = 0
for i in range(len(list)):
    if list[i] < list[min_num]:
        min_num = i
    elif list[i] > list[max_num]:
        max_num = i
if min_num > max_num:
    min_num, max_num = max_num, min_num

res = 0
for i in range(min_num + 1, max_num):
    res += list[i]
print(f"Сумма промежуточных элементов равна {res}")
