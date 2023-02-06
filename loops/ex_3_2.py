# Find the sum and product of the digits of the entered natural number. For example,
# if the number 325 is entered,
# then the sum of its digits is 10 (3+2+5), and the product is 30 (325).


num = int(input('input number: '))
len_num = len(str(num))
x = 0
count_nums = 0
for i in range(len_num):
    x = int(num) % 10
    num = num // 10
    count_nums += x
print(count_nums)




