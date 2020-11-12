import random

size = 10
min = 0
max = 100
list = [random.randint(min, max) for _ in range(size)]
print(list)

min_num = 0
max_num = 0
for i in range(len(list)):
    if list[i] < list[min_num]:
        min_num = i
    elif list[i] > list[max_num]:
        max_num = i
list[min_num], list[max_num] = list[max_num], list[min_num]
print(list)
