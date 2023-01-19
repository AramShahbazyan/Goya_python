# Write a program (calculator) that will accept 2 numbers and an action(+, -, *, /, **) , the program must return the
# result of the given action. for example num_1 = 3 num_2 = 5 action = ' + ' result = 8

while True:
    try:
        num_1 = int(input('enter number 1: '))
        action = input('enter action: ')
        if action == 'end':
            break
        num_2 = int(input('enter number 2: '))
        if action == "/" and num_2 == 0:
            print('division by zero')
            continue
        if action == '+':
            print(num_1 + num_2)
        elif action == '-':
            print(num_1 - num_2)
        elif action == '*':
            print(num_1 * num_2)
        elif action == '/':
            print(num_1 / num_2)
        elif action == '**':
            print(num_1 ** num_2)
        else:
            print('invalid action')
    except ValueError:
        print('please input numbers')
