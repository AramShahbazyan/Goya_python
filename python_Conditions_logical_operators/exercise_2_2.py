# Enter three integers from the keyboard. Decide which is the biggest.
try:
    a = int(input('input number 1: '))
    b = int(input('input number 2: '))
    c = int(input('input number 3: '))

    if a > b:
        if a > c:
            print(f'the biggest number is {a}')
        else:
            print(f'the biggest number is {c}')

    elif b > c:
        print(f'the biggest number is {b}')
    else:
        print(f'the biggest number is {c}')
except ValueError:
    print("ValueError: please input only numbers")
