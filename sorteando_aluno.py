#Author: Elaine Dias Pires

import string
from random import randint

line = str(input('Type the name of 4 students:\n')) #line that has been typeded by user

std = line.split(",", 3) #line splited
# print(std[0])
# print(std[1])
# print(std[2])
# print(std[3])
rand = randint(0,3)

print('The student that has been drawn is {} ' .format(std[rand]))

