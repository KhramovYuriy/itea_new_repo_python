'''users = [{"login": "admin",
          "password": "123123"},
         {"login": "admin2",
          "password": "123123"},
         {"login": "admin3",
          "password": "123123"}]

while True:
    choice = input("1 registration 2 login:")
    if choice == "1":
        # Запитуємо логін
        login = input("login:")
        # Запитуємо пароль
        password = input("password:")
        # Перевірка наявності користувача з подібним логіном
        if login not in [user["login"] for user in users]:
            # при відсутності
            user = {"login": login,
                    "password": password}
            # створити користувача
            users.append(user)
            # записати його до база даних

    if choice == "2":
        # Запитуємо логін
        login = input("login:")
        # Запитуємо пароль
        password = input("password:")
        # проходимось по користувачам
        for user in users:
            # звіряємо дані
            if login == user["login"] and password == user["password"]:
                print("Ви Увійшли !!!")
            # при співпадінні
            # виводимо напис Ви увійшли
'''


users = []

def user_menu():
    while True:
        new_choice = input("1 для виходу:")
        if new_choice == "1":
            break

def registration():
    login = input("login:")
    password = input("password:")
    if login not in [user["login"] for user in users]:
        user = {"login":login,
                "password":password}
        users.append(user)

def check_user(login,
               password,
               user):
    if (login == user["login"]
        and password == user["password"]):
        return True
    else:
        return False
def login():
    login = input("login:")
    password = input("password:")
    for user in users:
        if login == user["login"] and password == user["password"]:
            print("Ви Увійшли !!!")
            user_menu()


while True:
    choice = input("1 registration 2 login 3 exit:")
    if choice == "1":
        registration()

    if choice == "2":
        login()

    if choice == "3":
        break