# The coordinates (x;y) of the point and the radius of the circle (r) are entered. Determine
# whether a given point
# belongs to a circle if its center is at the origin.
try:
    r = int(input('input radius: '))
    x = int(input('input x: '))
    y = int(input('input y: '))

    if x ** 2 + y ** 2 == r ** 2:
        print('point belongs to a circle')
    else:
        print('point not belongs to a circle')
except ValueError:
    print('input only numbers')

