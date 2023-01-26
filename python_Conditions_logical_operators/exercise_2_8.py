# Enter an integer representing the character code according to the ASCII table. Determine if this is
# an English letter code or some other character.

num_1 = int(input('input number 1: '))
print(chr(num_1))
if (65 <= num_1 <= 90) or (97 <= num_1 <= 122):
    print(f'{num_1} is an English letter code')
else:
    print(f'{num_1} is not an English letter code')
