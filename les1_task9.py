x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
z = int(input("Введите третье число: "))
if y < x < z or z < x < y:
    print(f"Среднее число из введенных {x}")
elif x < y < z or z < y < x:
    print(f"Среднее число из введенных {y}")
else:
    print(f"Среднее число из введенных {z}")