num = int(input("Введиче номер буквы от 1 до 26, я назову вам букву: "))
num = ord("a") - 1 + num
print(f"Ваша буква {chr(num)}")