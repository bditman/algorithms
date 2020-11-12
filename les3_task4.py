import random

size = 30
min = 0
max = 10
list = [random.randint(min, max) for _ in range(size)]
print(list)

res = list[0]
freq = 1
for i in range(len(list)):
    count = 0
    for j in range(len(list)):
        if list[i] == list[j]:
            count += 1
    if count > freq:
        freq = count
        res = list[i]
print(f'Чаще всего стречается число {res}' if freq > 1 else 'Все числа уникальны')