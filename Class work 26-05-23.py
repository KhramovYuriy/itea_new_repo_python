items = [{"name":"Товар1",
          "description":"Опис товару",
          "price":180},
         {"name":"Товар2",
          "description":"Опис товару2",
          "price":110},
         {"name":"Товар3",
          "description":"Опис товару3",
          "price":130},
         {"name":"Товар4",
          "description":"Опис товару4",
          "price":150}]

for item in items:

    print(f"""Назва товару - {item['name']}
Опис товару - {item['description']}
Ціна товару - {item['price']}""")


"""items = [{"name":"Товар1",
          "description":"Опис товару",
          "price":180},
         {"name":"Товар2",
          "description":"Опис товару2",
          "price":110},
         {"name":"Товар3",
          "description":"Опис товару3",
          "price":130},
         {"name":"Товар4",
          "description":"Опис товару4",
          "price":150}]

for item in items:
    for key,value in item.items():
        print(f"{key} - {value}")

data = enumerate([1,2,3,4,5],1)
print(dict(data))

items = [{"name":"Назва товару",
          "description":"Опис товару",
          "price":100},
         {"name":"Назва товару2",
          "description":"Опис товару2",
          "price":120},
         {"name":"Назва товару3",
          "description":"Опис товару3",
          "price":130}]
for number,item in enumerate(items,1):
    print(f"{number} - {item['name']}")
number = input("выберете номер товара")
if number.isdigit() and 0 < int(number) <= len(items):
    item = items[int(number) - 1]
    keys = dict(enumerate(item.keys(),1))
    choice = int(input("1 name 2 descr 3 price"))
    if choice in keys:
        key = keys[choice]
        item[key] = input("новое значение")"""

"""users = ["User1",
         "User2",
         "User3",
         "User4"]
for user in users:
    print(f"Користувач - {user}")
for number,user in enumerate(users,5):
    print(f"{number}) - {user}")
for number,user in enumerate(users,1):
    print(f"{number}) - {user}")
choice = input("Оберіть номер користувача:")
if choice.isdigit() and 0 < int(choice) <= len(users):
    number = int(choice) - 1
print(f"выбраный пользователь - {users[number]}")"""

'''user = {"login":"User1",
        "password":"123123",
        "user_type":"admin",
        "user_data":[]}
print(dict(enumerate(user.keys(),1)))


for number,key in enumerate(user.keys(),1):
    print(f"{number}) - {key}")

keys = dict(enumerate(user.keys(),1))
choice = input("Обери який ключ ти бажаєш редагувати:")
if choice.isdigit() and int(choice) in keys:
    key = keys.get(int(choice))
    user[key] = input("нове значення:")
    print(user)'''

'''numbers = range(1,100000,100)
print(list(numbers))

for _ in range(5):
    print("Hello WOrld")

print([0   for number in range(1,1001)])
user_number = int(input("Введіть число:"))
print([f"User - {number}" for number in range(1,1001) if number < user_number])

numbers = set([1,2,3,4,5,6,7,8])
numbers2 = set([5,6,7,8,9,10,11,12])

print(numbers.intersection(numbers2))
'''
