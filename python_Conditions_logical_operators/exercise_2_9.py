# Based on the lengths of three segments entered by the user, determine the possibility
# of the existence of a triangle composed of these segments. If such a triangle exists, then
# determine whether it is scalene, isosceles, or equilateral.


try:
    size1 = int(input('input size 1: '))
    size2 = int(input('input size 2: '))
    size3 = int(input('input size 3: '))

    if size1 + size2 > size3 and size1 + size3 > size2 and size2 + size3 > size1:
        if size1 == size2 == size3:
            print('the triangle exists and is equilateral')
        elif size1 == size2 or size1 == size3 or size2 == size3:
            print('the triangle exists and is isosceles')
        else:
            print('the triangle exists and is scalene')
    else:
        print('the triangle is not exists')
except ValueError:
    print('please input only int numbers')

