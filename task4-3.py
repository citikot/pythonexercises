"""
Створіть функцію make_operation, яка приймає першим параметром простий арифметичний оператор
(для спрощення нехай це буде ‘+’, ‘-’ і ‘*’) у вигляді рядка та випадкову кількість аргументів 
(тільки цілі числа або числа з рухомою комою) другим параметром. Потім функція має повернути
результат додавання, віднімання та множення всіх чисел в другому параметрі.

Наприклад:
виклик make_operation(‘+’, 7, 7, 2) повинен повернути 16
виклик make_operation(‘-’, 5, 5, -10, -20) повинен повернути 30
виклик make_operation(‘*’, 7, 6) повинен повернути 42
Також треба додати валідацію введених параметрів і викликати відповідні помилки, якщо їхній тип неправильний.
"""

def make_operation(operator, *args):
     
    if type(operator) is not str:
        raise TypeError()
    elif operator not in ('+','-','*'):
        raise ValueError()
    
    result = args[0]
    
    for i in range(len(args) - 1):
        if not (isinstance(args[i], int) or isinstance(args[i], float) or isinstance(args[i+1], int) or isinstance(args[i+1], float)):
            raise ValueError()

        if operator == '+':
            result += args[i+1]
        elif operator == '-':
            result -= args[i+1]
        else:
            result *= args[i+1]
            
    return result
  
print(make_operation("-", 5, 5, -10, -20))
