#Author: Elaine Dias Pires

number = int (input('Please, type an number:'))

print('\nThe table of this number is: \n')

print('=' * 11)
for i in range(1,11) :
    print('{} x {:2} = {:02} ' .format(number, i, number * i))

print('=' * 11)