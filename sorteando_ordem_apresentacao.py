#Author: Elaine Dias Pires

import random

print('Type the name of 4 students:\n')
std1 = str(input('First student: '))
std2 = str(input('Second student: '))
std3 = str(input('Third student: '))
std4 = str(input('Fourth student: '))
print('\n')

list = [ std1, std2, std3, std4 ]

print('The order of presentation is:')

for i in range (0,4):
    ch = random.choice(list)
    print(ch)
    list.remove(ch)




