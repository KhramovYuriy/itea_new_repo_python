# LAMBDA ананимная функция
'''
def action (number1,number2):
    return number1 ** number2
'''
'''
my_action = lambda number1,number2:number1 ** number2
print(my_action(5,5))
'''

# print((lambda number1,number2:number1 ** number2)(5,5))
'''
import math

data = list(range(100))

def action(element):
    return math.sin(element) ** 4 + 5 - math.sin(element)

results = map(action,data)
print(list(results))
'''


import math

data = (number for number in range(10000000000000000000000000000000000000000000))

def action(element):
    return math.sin(element) ** 4 + 5 - math.sin(element)

results = map(action,data)
for result in results:
    print(result)