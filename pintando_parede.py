#Author: Elaine Dias Pires

l = float(input('Please, enter the width of a wall: '))
h = float(input('And now , the height of the wall: '))

area= l * h
quantity = area / 2
# 1l = 2m^2
print('The area of this wall is {} m2 ' .format(area))
print('To paint this entire wall, we\'ll need {:.3}l of paint ' .format(quantity))