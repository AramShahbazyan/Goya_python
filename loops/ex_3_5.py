# Display as many elements of the Fibonacci series as the user has specified. For example, if the input received the
# number 7, then the output should contain the first six numbers of the Fibonacci series: 1 1 2 3 5 8 13.

num = int(input('input number: '))
x = 0
ls = [1, 1]
for i in range(num-2):
    ls.append(ls[i] + ls[i + 1])
for i in range(len(ls)):
    print(ls[i], end=' ')



