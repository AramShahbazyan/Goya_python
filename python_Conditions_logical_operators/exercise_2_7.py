# Enter three different numbers from the keyboard. Find the average (greater than one but less than the other).

num_1 = int(input('input number 1: '))
num_2 = int(input('input number 2: '))
num_3 = int(input('input number 3: '))

if num_1 > num_2:
    if num_1 < num_3:
        print(num_1)
    elif num_2 > num_3:
        print(num_2)
    else:
        print(num_3)
elif num_2 < num_3:
    print(num_2)
elif num_1 > num_3:
    print(num_1)
else:
    print(num_3)
