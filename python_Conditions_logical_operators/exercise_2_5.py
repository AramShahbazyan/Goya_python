# Enter two random numbers from the keyboard, one even and the other odd. Decide and display an odd number.

num_1 = int(input('input number 1: '))
num_2 = int(input('input number 2: '))

if num_1 % 2 > 0:
    print(f'{num_1} is odd')
else:
    print(f'{num_2} is odd')