# Given the following function y=f(x):
# y = 2x - 10 if x > 0,  y = 0 if x = 0,  y = 2 * |x| — 1 if x < 0 It is required to
# find the value of the function by the passed x.

x = int(input('input x: '))
y = 0
if x > 0:
    y = 2 * x - 10
else:
    y = 2 * abs(x) - 1

print(y)
