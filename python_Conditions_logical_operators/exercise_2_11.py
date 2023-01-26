# Determine the quarter of the coordinate plane to which the point belongs.
# Enter point coordinates from the keyboard.


try:
    cord_x = int(input('input cord x: '))
    cord_y = int(input('input cord y: '))
    if cord_x == 0 or cord_y == 0:
        print('point does not belong to any quarter')
    else:
        if cord_x > 0:
            if cord_y > 0:
                print('point is in first quarter')
            else:
                print('point is in fourth quarter')
        else:
            if cord_y > 0:
                print('point is in second quarter')
            else:
                print('point is in third quarter')
except ValueError:
    print('please input only int numbers')
