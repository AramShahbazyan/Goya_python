# Write a program that checks if a string is a palindrome or not.

my_str = input('please input string: ')

half = len(my_str) // 2
ls = []
i = 1
for i in my_str:
    ls.append(i)
end_ind = -1
count = 0
for j in range(half):
    if ls[j] == ls[end_ind]:
        count += 1
        end_ind -= 1
if count == half:
    print(f'{my_str} is palindrome')
else:
    print(f'{my_str} is not palindrome')
