#Author: Elaine Dias Pires

number = int(input('Type a number: '))

print('The sucessor of {} is {} and the predecessor is {} . ' 
.format(number, number + 1, number - 1))

print('Twice this number is {}, its triple is {} and its sqare root is {:.3} ' 
.format(2*number, 3*number, number ** 0.5))
