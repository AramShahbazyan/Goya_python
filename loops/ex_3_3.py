# Print a series of natural numbers on the screen from minimum to maximum with a step. For example,
# if the minimum is 10, the maximum is 35, and the step is 5, then the output should be: 10 15 20 25 30 35.
# The user specifies the minimum, maximum, and step (read from the keyboard).

# x = list(map(int, input('input: ').split()))
# print(x)

minimum = int(input('input minimum number: '))
maximum = int(input('input maximum number: '))
step = int(input('input step: '))
y = minimum
while y <= maximum:
    print(y)
    y += step
