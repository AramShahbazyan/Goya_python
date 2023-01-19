# write a program that will solve the square equation.
# # a * x ** 2 + b * x + c = 0
import math

try:
    a = int(input('pleas input a: '))
    b = int(input('pleas input b: '))
    c = int(input('pleas input c: '))
    d = (b ** 2) - (4 * a * c)

    if d > 0:
        result_1 = (-b - (math.sqrt(d))) / (2 * a)
        result_2 = (-b + (math.sqrt(d))) / (2 * a)
        print(f'result_1 = {result_1}, result_2 = {result_2}')
    elif d == 0:
        result = (-b - (math.sqrt(d))) / (2 * a)
        print(f'result = {result}')
    else:
        print('has no solution')
except ValueError:
    print('please input only numbers')
