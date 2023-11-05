# lab 3
# var 3
# Виведення вертикальної гістограми, висота столбців якої відображає значенню розряду певного числа.
print("Введіть ваше число:")
while True:
    try:
        number = int(input())
    except:
        print("Помилка!\nСпробуйте ще раз!")
        continue
    if number <= 0:
        print("Помилка!\nЧисло повинно бути додатнім!\nСпробуйте ще раз!")
    else:
        break
if number <= 0:
    print("Помилка!\nЧисло повинно бути додатнім!")
    exit()
# Перевіряємо правильність введених даних.
print("Введіть ваш символ:")
i = input()
number = str(number)
print(' '.join(number))
# Додаємо після кожного елементу " ".
max_number = max(map(int, number))
# Функція map перетворює введені числа на список, max шукає найбільше значення.
for symbol in range(max_number, 0, -1):
# За допомогою функції range будуть перелічуватися числа від максимального до нуля, з кроком -1.
    line = ""
    for digit in number:
        if int(digit)>=symbol:
            line += i + " "
        else:
            line += "  "
    print(line)