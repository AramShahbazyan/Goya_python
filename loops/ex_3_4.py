# Calculate the factorial of the entered number.

num = int(input('input number: '))
fac = 1
for i in range(1, num + 1):
    fac *= i

print(fac)
