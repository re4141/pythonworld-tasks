# [RUS]: Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция,
# которая должна быть произведена над ними.
# Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить (первое на второе).
# В остальных случаях вернуть строку "Неизвестная операция".

# [ENG]: Write a function called 'arithmetic' that takes 3 args: the first 2 are numbers,
# the third one is an operation, which should be made over them.
# If the third argument is '+' so sum them, if '-' then substract, '*' - multiply; '/' - divide (first by second).
# In other cases, return the string 'Unknown operation'.


def arithmetic(x, y, oper):
    if oper == '*':
        return x*y
    elif oper == '/':
        return x/y
    elif oper == '+':
        return x+y
    elif oper == '-':
        return x-y
    else:
        return 'Unknown operation'

arithmetic(3,5,'+')