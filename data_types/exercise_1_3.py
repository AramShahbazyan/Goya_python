# Write a program that will take 2 numbers and will return True if the
# first number is greater than or equal to the other
# and will return False otherwise

try:
    a = int(input('please input nuber 1: '))
    b = int(input('please input nuber 2: '))
    if a >= b:
        print('True')
    else:
        print('False')
except:
    print('please input only int numbers')
