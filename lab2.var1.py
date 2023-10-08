# lab 2
# var 1
# Переведення чисел у різні системи числень

print("Введіть ціле число яке хочете перевести:")
try:
    number = int(input())
except:
    print("Помилка!\nСпробуйте ще раз!")
    exit()
print("Введіть систему числення:\n\"2\",\"8\",\"16\"")
try:
    system = int(input())
except:
    print("Помилка\nСпробуйте ще раз!")
    exit()
if system == 2:
    print(bin(number))
elif system == 8:
    print(oct(number))
elif system == 16:
    print(hex(number))
else:
    print("Введіть вашу систему численя коректно!")

# bin = 2
# oct = 8
# hex = 16