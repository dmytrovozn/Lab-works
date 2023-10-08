# lab 2
# var 3
# Переведення числа у гістограму з символів

print("Введіть ваше число:")
try:
    number = int(input())
except:
    print("Помилка!\nСпробуйте ще раз!")
    exit()
str_number = str(number)
for symbol in str_number:
    print("#! " * int(symbol))