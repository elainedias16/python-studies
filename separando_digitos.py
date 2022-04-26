#Author: Elaine Dias Pires

num = float(input('Type a number between 0 and 9999:\n'))
print('\n')

un = num % 10
ten = (num % 100) / 10
hu = int( num / 100 ) %10
th = num/ 1000

print('Unit:     '     ,  int(un))
print('Ten:      '      ,  int(ten))
print('Hundred:  '  ,  hu)
print('Thousand: ' ,  int(th))