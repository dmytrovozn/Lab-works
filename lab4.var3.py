# lab 4
# var 3
# Створення класів бібліотеки та книги.
# name = "назва книги"
# quantity = "кількість усіх сторінок книги"
# number = "номер сторінки, до якої книгу було прочитано"
# percent = "відсокток книги, який було прочитано"

class Book():
    def __init__(self, name, quantity, number, percent):
        self.name = name
        self.quantity = quantity
        self.number = number
        self.percent = percent
    
    def count(self):
        self.percent = round((int(self.number) / int(self.quantity)) * 100, 1)
    
"""Наприклад:"""
name1 = input("Введіть назву книги:\n")
while True:
    try:
        quantity1 = int(input("Введіть загальну кількість сторінок книги:\n"))
        number1 = int(input("Введіть кількість прочитаних сторінок:\n"))
    except:
        print("Помилка!\nСпробуйте ще раз!")
        continue
    if quantity1 < number1:
        print("Кількість прочитаних сторінок не може перевищувати загальну кількість сторінок!")
    else:
        break

book1 = Book(name1, quantity1, number1, None)
book1.count()
print("Відсоток книги, який було прочитано " + str(book1.percent) + "%")

class Library():
    def __init__(self, schedule):
        self.schedule = schedule
                    
    def add_book(self, book1):
        self.schedule.append(book1)  
        print("Книга додана до списку")
    def remove_book(self, book1):
        self.schedule.remove(book1)  
        print("Книга видалена зі списку")
    def show(self):
        print("Назва книги: " + str(book1.name) + " Cкільки відсотків книги було прочитано: " + str(book1.percent) + "%")
Library1 = Library([])

Library1.add_book(book1)

Library1.remove_book(book1)

Library1.show()
