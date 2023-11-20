# lab 5
# var 3
# Виведення всіх абзаців, що містять у собі введений користувачем тег.

with open(r"C:\Users\Admin\PycharmProjects\pythonProject\1\text.txt", "r", encoding="utf-8") as file:
    file_read = file.read()
while True:
    tag = input("Введіть ваш тег:\n")
    if "#" + tag not in file_read:     
        print("Помилка!Такого тегу немає!\nСпробуйте ще раз!")
    else:
        break
spleated_paragraphs = file_read.split("\n\n")
for paragraph in spleated_paragraphs:
    if "#" + tag in paragraph:
        print(paragraph)
