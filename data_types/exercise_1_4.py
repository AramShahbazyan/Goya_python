# Write a program that will take a five-digit number and will insert each digit in the
# given number in one list in order from beginning to end.
try:
    num = int(input("please input number: "))
    if len(str(num)) != 5:
        print('please input only five-digit number')
    else:
        my_list = []
        for i in range(5):
            x = num % 10
            num = num // 10
            my_list.append(x)
        sort_ls = sorted(my_list)
        print(sort_ls)

except:
    print('please input only int numbers')
