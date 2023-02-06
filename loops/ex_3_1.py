# Count the even and odd digits of the entered natural number. For example, if the number 34560 is entered,
# then it has 3 even digits (4, 6, and 0) and 2 odd digits (3 and 5).

num = int(input('input number: '))
odd_nums = 0
even_nums = 0
for i in str(num):
    if int(i) % 2 == 0:
        even_nums += 1
    else:
        odd_nums += 1

print(f'count odd nums = {odd_nums},  count even nums = {even_nums}')