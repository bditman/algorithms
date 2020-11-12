import random

size = 10
min = 0
max = 100
list = [random.randint(min, max) for _ in range(size)]
print(list)

res = []
for i in range(len(list)):
    if list[i] % 2 == 0:
        res.append(list[i])
print(f"Список с четными элементами {res}")