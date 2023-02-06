# Form the inverse of the entered number in the order of the digits included in it and display it. For example,
# if you entered the number 3486, then you need to output the number 6843. Without using string methods.

num = int(input('input number: '))

y = num
while y != 0:
    num = y % 10
    y = y // 10
    print(num, end='')
