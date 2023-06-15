'''
def my_action(text):
    print("1")
    print("2")
    print("3")
    print("4")
    print("5")
    print(text)

my_action(3)
'''
'''
def action():

    def action2():
        print("22222")
    action2()

    name = "1"
    password = "2"
    print(name)
    print(password)

    for number in range(1,10):
        print(number)

    action()

action()
'''
'''
# recursion_limit = 1022
def recursion_action():
    recursion_action()

recursion_action()
'''

'''
data = {"1":"1",
        "2":"2",
        "3":"3",
        "4":{"11":"11",
             "22":"22",
             "33":"33",
             "44":{}}}

def dict_worker(data):
    for key,value in data.items():
        if type(value) == dict:
            dict_worker(value)
        else:
            print(key,value)

dict_worker(data)
'''

# O n ** 2
'''
numbers = [3,2,4,1,5,6]
def buble_sort(data):
    for i in range(len(data)):
        for j in range(len(data)):
            if data[j] > data[i]:
                data[i],data[j] = data[j],data[i]
    return data
'''

'''
def quick_sort(data):
    if len(data) <= 1:
        return data

    left,right,center = [],[],[]
    center_element = data[0]
    for element in data:
        if element < center_element:
            left.append(element)
        if element > center_element:
            right.append(element)
        if element == center_element:
            center.append(element)
    return quick_sort(left) + center + quick_sort(right)
'''
'''
data = []
def new_action(action):

    def action2():
        if data:
            print("1")
            print("2")
            print("3")
            action()

    return action2

@new_action   #action = new_action(action)
def action():
    print("Hello WOrld")



action()

'''
'''

def decorator(action):
    def wrapper():
        print("1")
        action()

    return wrapper

@decorator
def action():
    print("Hello WOrld")


action()
'''
'''
articles = [1,2,3]

def article_exists(action):
    def wrapper():
        print("1") # Код який йде до
        return action() # action() - виконання функції яку доповнюємо
        print("-------------") # Код який йде після

    return wrapper

@article_exists   # read_article = article_exists(read_article)
def read_article():
    print("Читаємо")
    return 0


print(read_article())
'''
'''
data = []

def decorator1(action):
    def wrapper():
        if data:
            return action()
    return wrapper

def decorator2(action):
    def wrapper():
        print("-"*20)
        action()
        print("-"*20)
    return wrapper

@decorator1
@decorator2
def action1():
    print("Виконую щось")


@decorator2
@decorator1
def action2():
    print("1232132112")

action2()
'''
'''
data = [1,2,3,4,5,6]
data2 = [1,2,3,4]
data3 = []


def data_exists(data):
    def decorator(action):
        def wrapper():
            if data:
                action()
        return wrapper
    return decorator

@data_exists(data)
@data_exists(data2)
def action():
    print("1")

@data_exists(data2)
def action2():
    print("2")

@data_exists(data3)
def action3():
    print("3")

action()
'''
# *args
'''
def action(*args):
    print(args)
    for element in args:
        print(element)

action(1,2,3,4,5,6,7,8,9,0,10,123,123,123,213,213,213,21,213,21)
'''

# **kwargs
'''
def action2(**kwargs):
    print(kwargs)

action2(name="User",
        office="155",
        user_type="admin",
        new_type="2")
'''

'''
def best_action(*args,**kwargs):
    print(args,kwargs)


best_action(1,2,3,3,3,2,34,2342,34,234,234,23,23,2344,32,
            name="User",
            password="1231231312",
            office="155")

'''

'''
def decorator(action):
    def wrapper(*args,**kwargs):
        print("START") # Код перед
        action(*args,**kwargs) # Виконання нашої функції
        print("FINISH") # Код після
    return wrapper


@decorator
def action(text):
    print(text)

action("12321")
'''


# Список контактів
# прийняти дзвінок
# надіслати дзвінок
# переглянути журнал дзвінків
# Якщо контакт є буде виписувати його ім'я
# Якщо контакту немає юуде виписано номер

# КОНТАКТИ
# Записи про дзвінки


def data_exists(data):
    def decorator(action):
        def wrapper(*args, **kwargs):
            if data:
                action(*args, **kwargs)
            else:
                print("Непкорректна операція")

        return wrapper

    return decorator


records = []
contacts = []


# Контакт - словник з ключами Ім'я телефоня
# Запис про дзвінок словник ключі - ім'я  телефон статус (прийнято або надіслано)
@data_exists(contacts)
def get_contact_name(number):
    for contact in contacts:
        if contact["number"] == number:
            return contact["name"]

def update_record_names(number, name):
    for record in records:
        if record["number"] == number:
            record["name"] = name


def add_contact():
    contact = {"name": input("Введіть ім'я"),
               "number": input("Введіть номер телефону:")}
    contacts.append(contact)
    update_record_names(number=contact["number"],
                        name=contact["name"])

def add_record(number, status):
    name = get_contact_name(number)
    if not name:
        name = number
    record = {"name": name,
              "number": number,
              "status": status}
    records.append(record)
def call(number):
   add_record(number,"call")


def recieve(number):
    add_record(number, "receive")


@data_exists(records)
def show_calls():
    for record in records:
        print(f"""Зателефонував {record['name']}
З номером {record['number']}
Статсу дзвінка - {record['status']}""")


while True:
    choice = input(f"""1 додати контакт
2 зателефонувати
3 прийняти дзвінок
4 переглянути журнал
9 вихід:""")
    if choice == "1":
        add_contact()
    if choice == "2":
        number = input("Введіть номер:")
        call(number)
    if choice == "3":
        number = input("Введіть номер:")
        recieve(call)
    if choice == "4":
        show_calls()
    if choice == "9":
        break

