# The program generates a random integer from 0 to 100. The user must guess it in no more than 10 attempts.
# After each unsuccessful attempt, more or less the number entered by the user should be reported than what is guessed.
# If in 10 attempts the number is not guessed, then output the hidden number.

from random import randint

random_num = randint(0, 100)

i = 0
while i < 10:
    num = int(input('input number: '))
    if num == random_num:
        print(f'you are win, the hidden number is {num}')
        break
    elif num < random_num:
        print(f'{num} is less the hidden number')
    elif num > random_num:
        print(f'{num} is great the hidden number')

    i += 1
print(f'hidden number is {random_num}')
