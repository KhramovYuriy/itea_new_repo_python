# 1
'''
Записати у файл числа від 0 до 100
'''
# 2
'''
Прочитати текстовий файл назву якого має вказати користувач
'''
# 3
'''
Прочитати файл із зображення
Записати дані цього файлу під назвою 1.png
'''

# 1

f = open("db.txt","a")

for number in range(100):
f.close()




# 2
names = []

while True:
     choise = input("1.Створити новий файла або 2. пошуку файла 3. вихід : ")
     if choise == "1":
         name = input("Ведіть назву файла для створення: ")
         with open(name, "a") as file:
             names.append(name)
             print(names)
     if choise == "2":
         name = input("Введіть назву файлу для пошуку: ")
         if name in names:
             print("Файл знайдено.")
         else:
             print("Файл не знайдено.")

     if choise == "3":
         break
# 3

import os
print(os.path.exists("1.png"))
with open("1.png", "rb") as f:
     print(f.read())
with open("1.png", "rb") as f,\
     open("2.png","wb") as f2:
    f2.write(f.read())