import random

num = random.randint(0, 100)
print("Угадайте число от 0 до 100 за 10 попыток, вперед: ")
for i in range(1, 11):
    user_num = int(input(f"{i} попытка. Введите число: "))
    if num > user_num:
        print("Попробуй число побольше!")
    elif num < user_num:
        print("Попробуй число поменьше!")
    else:
        print(f"Вы выйграли. Попытка №{i}")
        break
else:
    print(f"В этот раз не повезло, число было {num}")

