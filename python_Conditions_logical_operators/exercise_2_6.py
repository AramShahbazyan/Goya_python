# Enter two non-zero integers from the keyboard. Check if the first is divisible by the second. Display a message
# about it, display the remainder after the division (if any) and the integer part after the division (whatever).

num_1 = int(input('input number 1: '))
num_2 = int(input('input number 2: '))

if num_2 % num_1 == 0:
    print(f'{num_1} is divisible by the {num_2} no remainder')
else:
    print(num_2 // num_1)
    print(num_2 % num_1)

