print("Давайте посчитаем сколько букв между теми которые вы ввели")
start = input("Введите начальную букву диапазона(латинские буквы): ")
finish = input("Введите последнюю букву диапазона(латинская буква, отличная от первой): ")
first = ord(start)
sec = ord(finish)
num = abs(first - sec) - 1
print(f"Между вашими буквами находится {num} других букв")